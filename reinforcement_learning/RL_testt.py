import gymnasium as gym
from stable_baselines3 import PPO
from gymnasium.envs.registration import register
from environment import PathfindingEnv

register(
    id="GridWorld-v1",
    entry_point=PathfindingEnv,
    kwargs={"size": 5} 
)
env= gym.make("GridWorld-v1",render_mode='human')
model=PPO.load("PPO-v0",env=env)
obs, info = env.reset()
while True:
    action, _states = model.predict(obs)  # Use learned policy
    obs, reward, done, _, _ = env.step(action)
    print(obs, reward, done, _, _)
    env.render()  # Show environment in real-time
    
    if done:
        break  # Start a new episode