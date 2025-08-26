"""
强化学习环境基类
"""

from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple, Any, Dict

class BaseEnv(ABC):
    """
    强化学习环境的基类，定义了环境的基本接口。
    """
    def __init__(self):
        self.state = None
        self.done = False
        self.info = {}
        
    @property
    @abstractmethod
    def state_dim(self) -> int:
        """状态空间维度"""
        pass
    
    @property
    @abstractmethod
    def action_dim(self) -> int:
        """动作空间维度"""
        pass
    
    @property
    @abstractmethod
    def action_space_type(self) -> str:
        """动作空间类型: 'discrete' 或 'continuous'"""
        pass
    
    @abstractmethod
    def reset(self) -> np.ndarray:
        """重置环境，返回初始状态"""
        pass
    
    @abstractmethod
    def step(self, action) -> Tuple[np.ndarray, float, bool, Dict]:
        """执行动作，返回(下一状态, 奖励, 是否结束, 信息)"""
        pass
    
    def render(self):
        """渲染环境（可选实现）"""
        pass
    
    def close(self):
        """关闭环境（可选实现）"""
        pass
    
    def seed(self, seed=None):
        """设置随机种子（可选实现）"""
        np.random.seed(seed)
        return [seed]
    
    
class CartPoleEnv(BaseEnv):
    """示例：简化的CartPole环境"""
    
    def __init__(self):
        super().__init__()
        self.gravity = 9.8
        self.masscart = 1.0
        self.masspole = 0.1
        self.total_mass = self.masspole + self.masscart
        self.length = 0.5
        self.polemass_length = self.masspole * self.length
        self.force_mag = 10.0
        self.tau = 0.02
        
        self.theta_threshold_radians = 12 * 2 * np.pi / 360
        self.x_threshold = 2.4
        
        self.state = None
        self.steps_beyond_done = None
        
    @property
    def state_dim(self) -> int:
        return 4  # [x, x_dot, theta, theta_dot]
    
    @property
    def action_dim(self) -> int:
        return 2  # [left, right]
    
    @property
    def action_space_type(self) -> str:
        return 'discrete'
    
    def reset(self) -> np.ndarray:
        self.state = np.random.uniform(low=-0.05, high=0.05, size=(4,))
        self.steps_beyond_done = None
        self.done = False
        return np.array(self.state, dtype=np.float32)
    
    def step(self, action) -> Tuple[np.ndarray, float, bool, Dict]:
        x, x_dot, theta, theta_dot = self.state
        force = self.force_mag if action == 1 else -self.force_mag
        
        costheta = np.cos(theta)
        sintheta = np.sin(theta)
        
        temp = (force + self.polemass_length * theta_dot ** 2 * sintheta) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta * temp) / (
            self.length * (4.0 / 3.0 - self.masspole * costheta ** 2 / self.total_mass)
        )
        xacc = temp - self.polemass_length * thetaacc * costheta / self.total_mass
        
        x = x + self.tau * x_dot
        x_dot = x_dot + self.tau * xacc
        theta = theta + self.tau * theta_dot
        theta_dot = theta_dot + self.tau * thetaacc
        
        self.state = (x, x_dot, theta, theta_dot)
        
        done = bool(
            x < -self.x_threshold
            or x > self.x_threshold
            or theta < -self.theta_threshold_radians
            or theta > self.theta_threshold_radians
        )
        
        reward = 1.0 if not done else 0.0
        
        return np.array(self.state, dtype=np.float32), reward, done, {}