from my_simple_env import *

env = mySimpleEnv()
for i in range(1000):
    env.update_obs(i)
    env.render(mode='human')