
from core import Player


from enum import Enum


class Color(Enum):
    white = 1
    empty = 0
    black = -1


class MorabarabaPlayer(object):
    name = "Dark"

    def __init__(self, color):
        self.color = color 
        self._reset_player_info()

    def _reset_player_info(self):
        self.pieces_in_hand = 12

    def play(self, state):
        raise NotImplementedError

    def set_score(self, new_score):
        self.score = new_score

    def update_player_infos(self, infos):
        self.in_hand = infos['in_hand']
        self.score = infos['score']

    def reset_player_informations(self):
        self.in_hand = 12
        self.score = 0

    def get_name(self):
        return self.name