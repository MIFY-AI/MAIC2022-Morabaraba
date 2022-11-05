"""
Created on 16 sept. 17:13 2020

@author: HaroldKS
"""

from typing import Tuple
from .utils import BoardStateGenerator as BSG
from core import Color
import numpy as np


# TODO: Update when moving to numpy

class Board(object):

    def __init__(self, board_shape, max_per_cell=1):

        self.board_shape = board_shape
        self._board_state = BSG.generate_empty_board(board_shape)
        self.max_per_cell = max_per_cell

    def get_board_state(self):
        return self._board_state

    def is_cell_on_board(self, cell: (int, int)):
        """Verify if a cell is on the board.

        Args:
            cell ((int, int)): The coordinates of the cell we want to empty.

        Returns:
            bool: True if the cell is on the board. False if not.
        """
        return 0 <= cell[0] < self.board_shape[0] and 0 <= cell[1] < self.board_shape[1]

    def empty_cell(self, cell: (int, int)):
        """Empty a cell on the board is empty.

        Args:
            cell ((int, int)): The coordinates of the cell we want to empty.
        """
        if self.is_cell_on_board(cell):
            self._board_state[cell] = Color.empty

    def get_cell_color(self, cell: (int, int)):
        """Give the color of a cell on the board.

        Args:
            cell ((int, int)): The coordinates of the cell we want to empty.

        Returns:
            color (Color): The color of the cell.
        """
        if self.is_cell_on_board(cell):
            return self._board_state[cell]

    def is_empty_cell(self, cell: (int, int)):
        return self.is_cell_on_board(cell) and self._board_state[cell] == Color.empty

    def get_all_empty_cells(self):
        return [tuple(cell) for cell in np.argwhere(self._board_state == Color.empty)]

    def fill_cell(self, cell: (int, int), color):
        if self.is_empty_cell(cell):
            self._board_state[cell] = color

    def get_player_pieces_on_board(self, color):
        assert isinstance(color, Color), "Color need to be a valid Color object"
        return [tuple(cell) for cell in np.argwhere(self._board_state == color)]

    def get_json_board(self):
        def color_name(x):
            return x.name
        name = np.vectorize(color_name)
        return name(self._board_state).tolist()

    def is_center(self, cell: (int, int)):
        return cell == (self.board_shape[0] // 2, self.board_shape[1] // 2)

    def get_opponent_neighbours(self, cell: (int, int)):
        pass

    def get_all_empty_cells_without_center(self):
        return [tuple(cell) for cell in np.argwhere(self._board_state == Color.empty) if tuple(cell) != (self.board_shape[0] // 2, self.board_shape[0] //2)]

        