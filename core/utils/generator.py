"""
Created on 16 sept. 16:51 2020

@author: HaroldKS
"""
import numpy as np

from typing import List
from core import Color


class BoardStateGenerator(object):

    @staticmethod
    def generate_empty_board(board_shape: (int, int)) -> np.ndarray : # TODO : Do I use numpy or lists ?

        return np.asarray([[Color.empty for _ in range(board_shape[1])] for _ in range(board_shape[0])])