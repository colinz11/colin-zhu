import gym
import universe

env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1)

oberservation_n = env.reset()

