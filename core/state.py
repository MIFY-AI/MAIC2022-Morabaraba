"""
Created on 16 sept. 17:19 2020

@author: HaroldKS
"""


class State(object):

    def __init__(self, board, latest_player=None, latest_move=None, next_player=None):

        self.board = board
        self._latest_player = latest_player
        self._latest_move = latest_move
        self._next_player = next_player
        self.score = {-1: 0, 1: 0}

    def get_board(self):
        return self.board

    def get_latest_player(self):
        return self._latest_player

    def get_latest_move(self):
        return self._latest_move

    def get_next_player(self):
        return self._next_player