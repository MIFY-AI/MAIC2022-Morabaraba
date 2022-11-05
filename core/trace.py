"""
Created on 16 sept. 15:33 2020

@author: HaroldKS
"""


class Trace:

    def __init__(self, game_name):

        self.winner = 0
        self.states = []
        self.final_score = {-1: 0, 1: 0}

    def register(self, state):
        raise NotImplemented




