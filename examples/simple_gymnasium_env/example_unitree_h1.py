import numpy as np
from loco_mujoco import LocoEnv
import gymnasium as gym

# create the environment and task
env = gym.make("LocoMujoco", env_name="UnitreeH1.run")

# get the dataset for the chosen environment and task
expert_data = env.create_dataset()

action_dim = env.action_space.shape[0]

env.reset()
env.render()
absorbing = False
i = 0

while True:
    if i == 1000 or absorbing:
        env.reset()
        i = 0
    action = np.random.randn(action_dim)
    nstate, _, absorbing, _, _ = env.step(action)

    env.render()
    i += 1
