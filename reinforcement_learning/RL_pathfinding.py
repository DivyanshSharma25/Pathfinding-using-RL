import gymnasium as gym
from stable_baselines3 import PPO
from gymnasium.envs.registration import register
from environment import PathfindingEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv
import os
from sb3_contrib import RecurrentPPO

if __name__ == "__main__":
    model_name='PPO-v0'
    env_id="GridWorld-v1"
    env_cls= PathfindingEnv
    PPO_cls=PPO
    register(
        id=env_id,
        entry_point=env_cls,
        kwargs={"size": 5} 
    )

    env = gym.make(env_id, render_mode='human')
    if os.path.exists(model_name+ ".zip"):
        print("Loading existing model")
        model = PPO_cls.load(model_name, env=env)
        model.set_env(env)
        
        print("Loaded existing model")
    else:
        model = PPO("MlpPolicy", env,ent_coef=0.01, verbose=1)
        
    #model = PPO("MultiInputPolicy",env, verbose=1,tensorboard_log="./ppo_tensorboard/")
    #model = PPO("MlpPolicy",env, verbose=1,tensorboard_log="./ppo_tensorboard/")
    
    grid=[[1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

    start_pos=[0,0]
    end_pos=[4,4]
    
    obs,info = env.reset()
    while True:
        print("started training")
        model.learn(total_timesteps=100000,reset_num_timesteps=False) 
        model.save(model_name) 
        print("saved model")