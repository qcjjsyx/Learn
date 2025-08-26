import torch
from torch import nn
from torchvision import transforms as T
from PIL import Image
import numpy as np
from pathlib import Path
from collections import deque
import random, datetime, os

# Gym is an OpenAI toolkit for RL
import gym
from gym.spaces import Box
from gym.wrappers import FrameStack

# NES Emulator for OpenAI Gym
from nes_py.wrappers import JoypadSpace

# Super Mario environment for OpenAI Gym
import gym_super_mario_bros

from tensordict import TensorDict
from torchrl.data import TensorDictReplayBuffer, LazyMemmapStorage

import time, datetime
import matplotlib.pyplot as plt

### Environment setup
if gym.__version__ < '0.26':
    env = gym_super_mario_bros.make("SuperMarioBros-1-1-v3", new_step_api=True)
else:
    env = gym_super_mario_bros.make("SuperMarioBros-1-1-v0", render_mode='rgb', apply_api_compatibility=True)
    
    
# Limit the action space to
# 0 - NOOP
# 1 - Right
env = JoypadSpace(env,[['right'],['right','A']])
env.reset()
next_state,reward,done,trunc,info = env.step(action=0)
print(f"{next_state.shape},\n {reward},\n {done},\n {info}")
   
### Environment Wrappers
class SkipFrame(gym.Wrapper):
    def __init__(self, env, skip):
        super().__init__(env)
        self._skip = skip
        
    def setp(self, action):
        total_reward = 0.0
        for _ in range(self._skip):
            obs, reward, done, trunc, info = self.env.step(action)
            total_reawrd += reward
            if done:
                break
        return obs, total_reward, done, trunc, info

## 变成灰度图像
class GrayScaleObservation(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        obs_space = self.observation_space.shape[:2]
        self.observation_space = Box(low=0, high=255, shape=obs_space, dtype=np.uint8)
        
        
    def permute_orientation(self,observation):
        observation = np.transpose(observation, (2,0,1))
        observation = torch.tensor(observation.copy(), dtype=torch.float32)
        return observation
    
    def observation(self, observation):
        observation = self.permute_orientation(observation)
        transform = T.Grayscale()
        observation = transform(observation)
        return observation
    
##下采样
class ResizeObservation(gym.ObservationWrapper):
    def __init__(self, env,shape):
        super().__init__(env)
        if isinstance(shape,int):
            self._shape = (shape, shape)
        else:
            self._shape = tuple(shape)
        obs_shape = self._shape+self.observation_space.shape[2:]
        self.observation_space = Box(low=0, high=255, shape=obs_shape, dtype=np.uint8)
        
    def observation(self, observation):
        transform = T.Compose([
            T.Resize(self._shape,antialias=True),
            T.Normalize(0,255),
        ])
        observation = transform(observation).squeeze(0)
        return observation
# Apply Wrappers to environment
env = SkipFrame(env, skip=4)
env = GrayScaleObservation(env)
env = ResizeObservation(env, shape=84)
if gym.__version__ < '0.26':
    env = FrameStack(env, num_stack=4, new_step_api=True)
else:
    env = FrameStack(env, num_stack=4)
    
    
# 智能体
class Mario():
    def __init__(self,state_dim,act_dim,save_dir):
        self.state_dim = state_dim
        self.act_dim = act_dim
        self.save_dir = save_dir
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.net = MarioNet(self.state_dim, self.act_dim).float().to(self.device)
        
        self.exploration_rate = 1.0  # Epsilon for epsilon-greedy action selection
        self.exploration_rate_decay = 0.995  # Decay rate for epsilon
        self.exploration_rate_min = 0.01
        self.curr_step = 0
        
        self.save_every = 5e5
        
        self.memory = TensorDictReplayBuffer(storage=LazyMemmapStorage(10000, device=torch.device("cpu")))
        self.batch_size = 32
        self.gamma = 0.9
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=0.00025)
        self.loss_fn = nn.SmoothL1Loss()
        
        self.burnin = 1e4  # min. experiences before training
        self.learn_every = 3  # no. of experiences between updates to Q_online
        self.sync_every = 1e4  # no. of experiences between Q_target & Q_online sync
        
    def update_Q_online(self, td_estimate, td_target):
        loss = self.loss_fn(td_estimate, td_target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss.item()
    
    def sync_Q_target(self):
        """Synchronize the target network with the online network"""
        self.net.target.load_state_dict(self.net.online.state_dict())
    
    def td_estimate(self,state,action):
        current_Q = self.net(state, model="online")[np.arange(0,self.batch_size), action]
        return current_Q
    
    @torch.no_grad()
    def td_target(self, reward, next_state, done):
        next_state_Q = self.net(next_state, model="online")
        best_action = torch.argmax(next_state_Q, axis=1)
        next_Q = self.net(next_state, model="target")[np.arange(0, self.batch_size), best_action]
        return (reward + (1 - done.float()) * self.gamma * next_Q).float()
        
        
    def act(self, state):
        """Given a state, choose an epsilon-greedy action
        Inputs:
        state(``LazyFrame``): A single observation of the current state, dimension is (state_dim)
        Outputs:
        ``action_idx`` (``int``): An integer representing which action Mario will perform 
        """
        if np.random.rand() < self.exploration_rate:
            # Choose a random action
            action_idx = np.random.randint(self.act_dim)
        else:
            state = state[0].__array__()if isinstance(state, tuple) else state.__array__()
            state = torch.tensor(state, dtype=torch.float32, device=self.device).unsqueeze(0)
            action_val = self.net(state,model="online")
            action_idx = torch.argmax(action_val, dim=1).item()
            
        self.exploration_rate *= self.exploration_rate_decay
        self.exploration_rate = max(self.exploration_rate, self.exploration_rate_min)
        
        self.curr_step += 1
        return action_idx
            
    def cache(self, state,next_state,action,reward,done):
        """
        Store the experience to self.memory (replay buffer)

        Inputs:
        state (``LazyFrame``),
        next_state (``LazyFrame``),
        action (``int``),
        reward (``float``),
        done(``bool``))
        """
        def first_if_tuple(x):
            return x[0] if isinstance(x, tuple) else x
        state  = first_if_tuple(state).__array__()
        next_state = first_if_tuple(next_state).__array__()
        
        state = torch.tensor(state)
        next_state = torch.tensor(next_state)
        action = torch.tensor([action])
        reward = torch.tensor([reward])
        done = torch.tensor([done])

        self.memory.add(
            TensorDict({
                'state': state,
                'next_state': next_state,
                'action': action,
                'reward': reward,
                'done': done
            },batch_size=[])
        )

    def recall(self):
        """Sample experiences from memory"""
        """
        Retrieve a batch of experiences from memory
        """
        batch = self.memory.sample(self.batch_size).to(self.device)
        state = batch.get("state")
        next_state = batch.get("next_state")
        action = batch.get("action").squeeze()
        reward = batch.get("reward").squeeze()
        done = batch.get("done").squeeze()
        return state, next_state, action, reward, done

    def learn(self):
        """Update online action value (Q) function with a batch of experiences"""
        if self.curr_step % self.sync_every == 0:
            self.sync_Q_target()

        if self.curr_step % self.save_every == 0:
            self.save()

        if self.curr_step < self.burnin:
            return None, None

        if self.curr_step % self.learn_every != 0:
            return None, None

        # Sample from memory
        state, next_state, action, reward, done = self.recall()
        # print(f"state: {state.shape}, next_state: {next_state.shape}, action: {action.shape}, reward: {reward.shape}, done: {done.shape}")
        # Get TD Estimate
        td_est = self.td_estimate(state, action)

        # Get TD Target
        td_tgt = self.td_target(reward, next_state, done)

        # Backpropagate loss through Q_online
        loss = self.update_Q_online(td_est, td_tgt)

        return (td_est.mean().item(), loss)
    def save(self):
        save_path = (
            self.save_dir / f"mario_net_{int(self.curr_step // self.save_every)}.chkpt"
        )
        torch.save(
            dict(model=self.net.state_dict(), exploration_rate=self.exploration_rate),
            save_path,
        )
        print(f"MarioNet saved to {save_path} at step {self.curr_step}")
        
    
#神经网络
class MarioNet(nn.Module):
    """mini CNN structure
  input -> (conv2d + relu) x 3 -> flatten -> (dense + relu) x 2 -> output
  """
    def __init__(self, input_dim, out_dim):
        super(MarioNet, self).__init__()
        c, h, w = input_dim
        if h != 84:
            raise ValueError(f"Expecting input height: 84, got: {h}")
        if w != 84:
            raise ValueError(f"Expecting input width: 84, got: {w}")

        self.online = self.__build_cnn(c, out_dim)
        
        self.target = self.__build_cnn(c, out_dim)
        self.target.load_state_dict(self.online.state_dict())
        # Q_target parameters are frozen.
        for p in self.target.parameters():
            p.requires_grad = False
            
    def forward(self, x, model):
        if model == "online":
            return self.online(x)
        elif model == "target":
            return self.target(x)
            
    def __build_cnn(self, c, out_dim):
        return nn.Sequential(
            nn.Conv2d(in_channels=c, out_channels=32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(3136, 512),
            nn.ReLU(),
            nn.Linear(512, out_dim),
        )
            
class MetricLogger:
    def __init__(self, save_dir):
        self.save_log = save_dir / "log"
        with open(self.save_log, "w") as f:
            f.write(
                f"{'Episode':>8}{'Step':>8}{'Epsilon':>10}{'MeanReward':>15}"
                f"{'MeanLength':>15}{'MeanLoss':>15}{'MeanQValue':>15}"
                f"{'TimeDelta':>15}{'Time':>20}\n"
            )
        self.ep_rewards_plot = save_dir / "reward_plot.jpg"
        self.ep_lengths_plot = save_dir / "length_plot.jpg"
        self.ep_avg_losses_plot = save_dir / "loss_plot.jpg"
        self.ep_avg_qs_plot = save_dir / "q_plot.jpg"

        # History metrics
        self.ep_rewards = []
        self.ep_lengths = []
        self.ep_avg_losses = []
        self.ep_avg_qs = []

        # Moving averages, added for every call to record()
        self.moving_avg_ep_rewards = []
        self.moving_avg_ep_lengths = []
        self.moving_avg_ep_avg_losses = []
        self.moving_avg_ep_avg_qs = []

        # Current episode metric
        self.init_episode()

        # Timing
        self.record_time = time.time()

    def log_step(self, reward, loss, q):
        self.curr_ep_reward += reward
        self.curr_ep_length += 1
        if loss:
            self.curr_ep_loss += loss
            self.curr_ep_q += q
            self.curr_ep_loss_length += 1

    def log_episode(self):
        "Mark end of episode"
        self.ep_rewards.append(self.curr_ep_reward)
        self.ep_lengths.append(self.curr_ep_length)
        if self.curr_ep_loss_length == 0:
            ep_avg_loss = 0
            ep_avg_q = 0
        else:
            ep_avg_loss = np.round(self.curr_ep_loss / self.curr_ep_loss_length, 5)
            ep_avg_q = np.round(self.curr_ep_q / self.curr_ep_loss_length, 5)
        self.ep_avg_losses.append(ep_avg_loss)
        self.ep_avg_qs.append(ep_avg_q)

        self.init_episode()

    def init_episode(self):
        self.curr_ep_reward = 0.0
        self.curr_ep_length = 0
        self.curr_ep_loss = 0.0
        self.curr_ep_q = 0.0
        self.curr_ep_loss_length = 0

    def record(self, episode, epsilon, step):
        mean_ep_reward = np.round(np.mean(self.ep_rewards[-100:]), 3)
        mean_ep_length = np.round(np.mean(self.ep_lengths[-100:]), 3)
        mean_ep_loss = np.round(np.mean(self.ep_avg_losses[-100:]), 3)
        mean_ep_q = np.round(np.mean(self.ep_avg_qs[-100:]), 3)
        self.moving_avg_ep_rewards.append(mean_ep_reward)
        self.moving_avg_ep_lengths.append(mean_ep_length)
        self.moving_avg_ep_avg_losses.append(mean_ep_loss)
        self.moving_avg_ep_avg_qs.append(mean_ep_q)

        last_record_time = self.record_time
        self.record_time = time.time()
        time_since_last_record = np.round(self.record_time - last_record_time, 3)

        print(
            f"Episode {episode} - "
            f"Step {step} - "
            f"Epsilon {epsilon} - "
            f"Mean Reward {mean_ep_reward} - "
            f"Mean Length {mean_ep_length} - "
            f"Mean Loss {mean_ep_loss} - "
            f"Mean Q Value {mean_ep_q} - "
            f"Time Delta {time_since_last_record} - "
            f"Time {datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}"
        )

        with open(self.save_log, "a") as f:
            f.write(
                f"{episode:8d}{step:8d}{epsilon:10.3f}"
                f"{mean_ep_reward:15.3f}{mean_ep_length:15.3f}{mean_ep_loss:15.3f}{mean_ep_q:15.3f}"
                f"{time_since_last_record:15.3f}"
                f"{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'):>20}\n"
            )

        for metric in ["ep_lengths", "ep_avg_losses", "ep_avg_qs", "ep_rewards"]:
            plt.clf()
            plt.plot(getattr(self, f"moving_avg_{metric}"), label=f"moving_avg_{metric}")
            plt.legend()
            plt.savefig(getattr(self, f"{metric}_plot"))
            
            
use_cuda = torch.cuda.is_available()
print(f"Using CUDA: {use_cuda}")
print()

save_dir = Path("checkpoints") / datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
save_dir.mkdir(parents=True)

mario = Mario(state_dim=(4, 84, 84), act_dim=env.action_space.n, save_dir=save_dir)

logger = MetricLogger(save_dir)

episodes = 40000
for e in range(episodes):

    state = env.reset()

    # Play the game!
    while True:

        # Run agent on the state
        action = mario.act(state)

        # Agent performs action
        next_state, reward, done, trunc, info = env.step(action)

        # Remember
        mario.cache(state, next_state, action, reward, done)

        # Learn
        q, loss = mario.learn()

        # Logging
        logger.log_step(reward, loss, q)

        # Update state
        state = next_state

        # Check if end of game
        if done or info["flag_get"]:
            break

    logger.log_episode()

    if (e % 20 == 0) or (e == episodes - 1):
        logger.record(episode=e, epsilon=mario.exploration_rate, step=mario.curr_step)
        
        
        
from gym.wrappers import RecordVideo

video_dir = "videos"
os.makedirs(video_dir, exist_ok=True)

# 创建带视频记录的新环境
if gym.__version__ < '0.26':
    test_env = gym_super_mario_bros.make("SuperMarioBros-1-1-v3", new_step_api=True)
else:
    test_env = gym_super_mario_bros.make("SuperMarioBros-1-1-v0", render_mode='rgb', apply_api_compatibility=True)

test_env = JoypadSpace(test_env, [['right'], ['right', 'A']])
test_env = SkipFrame(test_env, skip=4)
test_env = GrayScaleObservation(test_env)
test_env = ResizeObservation(test_env, shape=84)
if gym.__version__ < '0.26':
    test_env = FrameStack(test_env, num_stack=4, new_step_api=True)
else:
    test_env = FrameStack(test_env, num_stack=4)

test_env = RecordVideo(test_env, video_dir, episode_trigger=lambda episode_id: True)

state = test_env.reset()
total_reward = 0
while True:
    # 用贪心策略选择动作
    state_arr = state[0].__array__() if isinstance(state, tuple) else state.__array__()
    state_tensor = torch.tensor(state_arr, dtype=torch.float32, device=mario.device).unsqueeze(0)
    action = torch.argmax(mario.net(state_tensor, model="online"), dim=1).item()
    next_state, reward, done, trunc, info = test_env.step(action)
    total_reward += reward
    state = next_state
    if done or info.get("flag_get", False):
        break

print(f"测试完成，总奖励: {total_reward}")
print(f"视频已保存到: {video_dir}")
test_env.close()