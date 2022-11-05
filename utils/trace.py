"""
Created on 30 oct. 18:37 2020

@author: HaroldKS
"""
import copy
import pickle


class Trace:

    def __init__(self, state, players):
        self.done = False
        self.players = players
        self.actions = [copy.deepcopy(state)]

    def add(self, state):
        self.actions.append(copy.deepcopy(state))

    def write(self, f):
        print(f)
        pickle.dump(self, open(f + ".trace", 'wb'))

    def load(self, f):
        return pickle.load(open(f, 'rb'))

    def get_actions(self):
        return self.actions

    def get_last_board(self):
        return self.actions[-1]