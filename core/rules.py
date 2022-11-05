"""
Created on 16 sept. 17:29 2020

@author: HaroldKS
"""


class Rule(object):

    @staticmethod
    def is_legal_move(state, action, player):
        raise NotImplementedError

    @staticmethod
    def get_player_actions(state, player):
        raise NotImplemented
