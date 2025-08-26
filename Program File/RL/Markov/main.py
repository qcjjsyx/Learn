import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import ListedColormap
import seaborn as sns

class GridWorld:
    def __init__(self, height=4, width=4, start=(0,0), goal=(3,3), obstacles=None, rewards=None):
        self.height = height
        self.width = width
        self.start = start
        self.goal = goal
        self.obstacles = obstacles if obstacles else [(1,1), (2,2)]
        
        # 动作空间：上、下、左、右
        self.actions = ['up', 'down', 'left', 'right']
        self.action_effects = {
            'up': (-1, 0),
            'down': (1, 0), 
            'left': (0, -1),
            'right': (0, 1)
        }
        
        # 奖励设置
        self.rewards = self._init_rewards(rewards)
        
        # 状态空间
        self.states = [(i, j) for i in range(height) for j in range(width) 
                      if (i, j) not in self.obstacles]
        self.n_states = len(self.states)
        self.state_to_idx = {state: idx for idx, state in enumerate(self.states)}
        
    def _init_rewards(self, rewards):
        if rewards is None:
            reward_grid = np.full((self.height, self.width), -0.1)  # 小负奖励鼓励快速到达目标
            reward_grid[self.goal] = 10.0  # 目标奖励
            for obs in self.obstacles:
                reward_grid[obs] = -10.0  # 障碍物惩罚
            return reward_grid
        return rewards
    
    def get_next_state(self, state, action):
        """获取执行动作后的下一个状态"""
        if state == self.goal or state in self.obstacles:
            return state
            
        dr, dc = self.action_effects[action]
        next_r, next_c = state[0] + dr, state[1] + dc
        
        # 检查边界
        if 0 <= next_r < self.height and 0 <= next_c < self.width:
            next_state = (next_r, next_c)
            # 检查是否撞到障碍物
            if next_state not in self.obstacles:
                return next_state
        
        return state  # 撞墙或撞障碍物则留在原地
    
    def get_reward(self, state, action, next_state):
        """获取奖励"""
        return self.rewards[next_state]
    
    def is_terminal(self, state):
        """判断是否为终止状态"""
        return state == self.goal

class MDPSolver:
    def __init__(self, env, gamma=0.9, theta=1e-6):
        self.env = env
        self.gamma = gamma
        self.theta = theta  # 收敛阈值
        
        # 初始化价值函数和策略
        self.V = np.zeros((env.height, env.width))
        self.policy = np.random.choice(env.actions, size=(env.height, env.width))
        
    def policy_evaluation(self, policy=None, max_iter=1000):
        """策略评估"""
        if policy is None:
            policy = self.policy
            
        V = np.copy(self.V)
        
        for iteration in range(max_iter):
            delta = 0
            V_new = np.copy(V)
            
            for state in self.env.states:
                if self.env.is_terminal(state):
                    continue
                    
                r, c = state
                action = policy[r, c]
                
                # 计算价值
                next_state = self.env.get_next_state(state, action)
                reward = self.env.get_reward(state, action, next_state)
                new_value = reward + self.gamma * V[next_state]
                
                delta = max(delta, abs(V_new[r, c] - new_value))
                V_new[r, c] = new_value
            
            V = V_new
            if delta < self.theta:
                print(f"策略评估收敛，迭代次数: {iteration + 1}")
                break
                
        return V
    
    def policy_improvement(self, V):
        """策略改进"""
        policy_stable = True
        new_policy = np.copy(self.policy)
        
        for state in self.env.states:
            if self.env.is_terminal(state):
                continue
                
            r, c = state
            old_action = self.policy[r, c]
            
            # 计算每个动作的Q值
            action_values = []
            for action in self.env.actions:
                next_state = self.env.get_next_state(state, action)
                reward = self.env.get_reward(state, action, next_state)
                q_value = reward + self.gamma * V[next_state]
                action_values.append(q_value)
            
            # 选择最佳动作
            best_action_idx = np.argmax(action_values)
            best_action = self.env.actions[best_action_idx]
            new_policy[r, c] = best_action
            
            if old_action != best_action:
                policy_stable = False
        
        return new_policy, policy_stable
    
    def policy_iteration(self, max_iter=100):
        """策略迭代算法"""
        print("开始策略迭代...")
        
        for iteration in range(max_iter):
            print(f"\n策略迭代第 {iteration + 1} 轮:")
            
            # 策略评估
            self.V = self.policy_evaluation(self.policy)
            
            # 策略改进
            new_policy, policy_stable = self.policy_improvement(self.V)
            self.policy = new_policy
            
            if policy_stable:
                print(f"策略迭代收敛，总迭代次数: {iteration + 1}")
                break
        
        return self.V, self.policy
    
    def value_iteration(self, max_iter=1000):
        """价值迭代算法"""
        print("开始价值迭代...")
        V = np.copy(self.V)
        
        for iteration in range(max_iter):
            delta = 0
            V_new = np.copy(V)
            
            for state in self.env.states:
                if self.env.is_terminal(state):
                    continue
                    
                r, c = state
                
                # 计算所有动作的Q值
                action_values = []
                for action in self.env.actions:
                    next_state = self.env.get_next_state(state, action)
                    reward = self.env.get_reward(state, action, next_state)
                    q_value = reward + self.gamma * V[next_state]
                    action_values.append(q_value)
                
                # 取最大值
                new_value = max(action_values)
                delta = max(delta, abs(V_new[r, c] - new_value))
                V_new[r, c] = new_value
            
            V = V_new
            
            if delta < self.theta:
                print(f"价值迭代收敛，迭代次数: {iteration + 1}")
                break
        
        # 提取最优策略
        optimal_policy = np.full((self.env.height, self.env.width), '', dtype=object)
        for state in self.env.states:
            if self.env.is_terminal(state):
                continue
                
            r, c = state
            action_values = []
            for action in self.env.actions:
                next_state = self.env.get_next_state(state, action)
                reward = self.env.get_reward(state, action, next_state)
                q_value = reward + self.gamma * V[next_state]
                action_values.append(q_value)
            
            best_action_idx = np.argmax(action_values)
            optimal_policy[r, c] = self.env.actions[best_action_idx]
        
        self.V = V
        self.policy = optimal_policy
        return V, optimal_policy

class Visualizer:
    def __init__(self, env):
        self.env = env
        
    def plot_grid_world(self, V=None, policy=None, title="Grid World"):
        """可视化网格世界"""
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        
        # 绘制网格
        for i in range(self.env.height + 1):
            ax.axhline(y=i, color='black', linewidth=1)
        for j in range(self.env.width + 1):
            ax.axvline(x=j, color='black', linewidth=1)
        
        # 绘制状态值
        if V is not None:
            for i in range(self.env.height):
                for j in range(self.env.width):
                    if (i, j) not in self.env.obstacles:
                        # 颜色映射价值
                        value = V[i, j]
                        color_intensity = (value - V.min()) / (V.max() - V.min()) if V.max() != V.min() else 0.5
                        color = plt.cm.RdYlGn(color_intensity)
                        
                        rect = patches.Rectangle((j, self.env.height-1-i), 1, 1, 
                                               linewidth=1, edgecolor='black', 
                                               facecolor=color, alpha=0.7)
                        ax.add_patch(rect)
                        
                        # 显示数值
                        ax.text(j + 0.5, self.env.height-1-i + 0.7, f'{value:.2f}', 
                               ha='center', va='center', fontsize=10, fontweight='bold')
        
        # 绘制策略箭头
        if policy is not None:
            arrow_map = {
                'up': (0, 0.3),
                'down': (0, -0.3),
                'left': (-0.3, 0),
                'right': (0.3, 0)
            }
            
            for i in range(self.env.height):
                for j in range(self.env.width):
                    if (i, j) not in self.env.obstacles and not self.env.is_terminal((i, j)):
                        action = policy[i, j]
                        if action in arrow_map:
                            dx, dy = arrow_map[action]
                            ax.arrow(j + 0.5, self.env.height-1-i + 0.3, dx, dy,
                                   head_width=0.1, head_length=0.1, fc='blue', ec='blue')
        
        # 标记特殊位置
        # 起点
        start_r, start_c = self.env.start
        ax.text(start_c + 0.5, self.env.height-1-start_r + 0.1, 'S', 
               ha='center', va='center', fontsize=16, fontweight='bold', color='green')
        
        # 终点
        goal_r, goal_c = self.env.goal
        ax.text(goal_c + 0.5, self.env.height-1-goal_r + 0.1, 'G', 
               ha='center', va='center', fontsize=16, fontweight='bold', color='red')
        
        # 障碍物
        for obs_r, obs_c in self.env.obstacles:
            rect = patches.Rectangle((obs_c, self.env.height-1-obs_r), 1, 1, 
                                   linewidth=2, edgecolor='black', 
                                   facecolor='black', alpha=0.8)
            ax.add_patch(rect)
        
        ax.set_xlim(0, self.env.width)
        ax.set_ylim(0, self.env.height)
        ax.set_aspect('equal')
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.tight_layout()
        plt.show()

def main():
    # 创建网格世界环境
    env = GridWorld(height=4, width=4, start=(0,0), goal=(3,3), 
                   obstacles=[(1,1), (2,2)])
    
    # 创建可视化器
    viz = Visualizer(env)
    
    # 显示初始环境
    print("网格世界环境:")
    print("S: 起点, G: 终点, 黑色: 障碍物")
    viz.plot_grid_world(title="初始网格世界环境")
    
    # 创建MDP求解器
    solver = MDPSolver(env, gamma=0.9)
    
    print("\n" + "="*50)
    print("运行策略迭代算法")
    print("="*50)
    
    # 策略迭代
    V_pi, policy_pi = solver.policy_iteration()
    viz.plot_grid_world(V_pi, policy_pi, title="策略迭代结果")
    
    print("\n" + "="*50)
    print("运行价值迭代算法")
    print("="*50)
    
    # 重新初始化求解器
    solver = MDPSolver(env, gamma=0.9)
    
    # 价值迭代
    V_vi, policy_vi = solver.value_iteration()
    viz.plot_grid_world(V_vi, policy_vi, title="价值迭代结果")
    
    # 比较结果
    print("\n" + "="*50)
    print("结果比较")
    print("="*50)
    print("策略迭代最终价值函数:")
    print(V_pi)
    print("\n价值迭代最终价值函数:")
    print(V_vi)
    
    print(f"\n价值函数差异 (最大): {np.max(np.abs(V_pi - V_vi)):.6f}")

if __name__ == "__main__":
    main()