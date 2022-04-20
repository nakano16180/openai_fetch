import gym
import gym_robotics

env = gym.make('FetchReach-v1')
while True:
    observation = env.reset()
    while True:
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Done!")
            break