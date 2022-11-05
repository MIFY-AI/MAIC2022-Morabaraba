"""
Created on 16 sept. 13:40 2020

@author: HaroldKS
"""


class BoardEnv(object):

    action_space = None
    observation_space = None
    score = {-1: 0, 1:0}

    def step(self, action):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError