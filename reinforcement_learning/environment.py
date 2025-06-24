import gymnasium as gym
from gymnasium import spaces
import numpy as np
import random
import sys
import copy
sys.path.append(".")
from a_star import a_star
class PathfindingEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}
    def dist(self,p1,p2):
        return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])
    def __init__(self, size=100,render_mode=None):
        super(PathfindingEnv, self).__init__()
        self.render_mode = render_mode
        self.size = size
        self.observation_space =spaces.Box(low=0, high=3, shape=(size,size), dtype=np.int32)
        self.action_space = spaces.Discrete(4)  # Right, Up, Left, Down
        self.grid = None
        self.c_step=0
        self.max_steps = 50
        self.total_reward=0
        self.path=[]
    def reset(self,options=None, seed=None):
        #super().reset(seed=seed)
        
        # grid=None
        # start_pos=None
        # end_pos=None
        # if options is not None:
        #     grid=options['grid']
        #     start_pos=options['start_pos']
        #     end_pos=options['end_pos']
        # if  grid is None :
        #     if self.grid is None:
        #         self.grid = np.ones((self.size, self.size), dtype=np.int32)
                
        # else:
        #     print("Using provided grid and positions")
        #     self.grid = grid
        #     self.start_pos = start_pos
        #     self.end_pos = end_pos
        path=None
        while True:
            self.grid = np.ones(shape=(self.size,self.size))
            n_obstacle=np.random.randint(6,8)
            #n_obstacle=0
            for _ in range(n_obstacle):
                while True:
                    x = random.randint(0, self.size - 1)
                    y = random.randint(0, self.size - 1)
                    if self.grid[y][x] == 1:
                        self.grid[y][x]= 0
                        break
            binary_grid=copy.deepcopy(self.grid)
            while True:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                if self.grid[y][x] == 1:
                    self.start_pos = [x, y]
                    self.grid[y][x]=2
                    break
            while True:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                if self.grid[y][x] == 1 and [x,y] != self.start_pos:
                    self.end_pos = [x, y]
                    self.grid[y][x]=3
                    break
            
            path,_=a_star(binary_grid.astype(np.int32).tolist(), self.start_pos, self.end_pos)

            if ((path != []) and (path is not None) ) and (len(path)>5):
                print(path)
                print(len(path),len(path)>5)
                break
        self.c_step = 0
        print(self.grid,self.start_pos,self.end_pos)
        print(self.total_reward)
        self.total_reward=0
        self.path=[]
        return self.grid, {}

    def step(self, action):
        self.c_step+=1
        reward=0
        pos=[0,0]
        print(action,self.start_pos,self.end_pos)
        if action == 0:
            if self.start_pos[0] < self.size - 1:
                if self.grid[self.start_pos[1]][ self.start_pos[0]+1] != 0:
                    pos[0] = 1
                else:
                    reward +=-0.3
            else:
                reward += -0.3
                # Right
        elif action == 1: 
            if self.start_pos[1] < self.size - 1:
                if self.grid[self.start_pos[1]+1][self.start_pos[0]] != 0:
                    pos[1] = 1
                else:
                    reward +=-0.3
            else:
                reward += -0.3
                # Up
            
        elif action == 2: 
            if self.start_pos[0] > 0:
                if self.grid[self.start_pos[1]][ self.start_pos[0]-1]!= 0:
                    pos[0] = -1
                else:
                    reward +=-0.3
            else:
                reward += -0.3
                # Left
            
        elif action == 3:
            if self.start_pos[1] > 0:
                if self.grid[self.start_pos[1]-1][self.start_pos[0]] !=0:
                    pos[1] = -1
                else:
                    reward +=-0.3
            else:
                reward += -0.3
                # Down   
            
        
        if self.dist(self.start_pos, self.end_pos) > self.dist([self.start_pos[0]+pos[0],self.start_pos[1]+pos[1]], self.end_pos):
            reward += 0
        
        self.grid[self.start_pos[1]][self.start_pos[0]]=1
        self.start_pos=[self.start_pos[0]+pos[0],self.start_pos[1]+pos[1]]
        self.grid[self.start_pos[1]][self.start_pos[0]]=2
        if self.start_pos in self.path:
            reward-=0.3
            
        self.path.append(self.start_pos)
        
        done = np.array_equal(self.start_pos, self.end_pos)
        if done:
            reward += 1
        else:
            reward -= 0.02
        if not done and self.c_step >= self.max_steps:
            done=True
            reward -= 1
        
        self.total_reward += reward
        return self.grid, reward, done, False, {}

    def render(self):
        print(f"Agent: {self.start_pos}, Target: {self.end_pos}")
