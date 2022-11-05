
from core import Board

from core.utils import BoardStateGenerator as BSG
from core import Color
import numpy as np

class MorabarabaBoard(Board):

    def __init__(self, board_shape, max_per_cell=1):

        self.board_shape = board_shape
        self._board_state = BSG.generate_empty_board(board_shape)
        self.max_per_cell = max_per_cell

        val = '_'
        size = (7,7)
        self.tab = np.array([   [0, '-', '-', 0, '-', '-', 0,],
                                ['-', 0, '-', 0, '-', 0, '-',],
                                ['-', '-', 0, 0, 0, '-', '-',],
                                [0, 0, 0, '-', 0, 0, 0,],
                                ['-', '-', 0, 0, 0, '-', '-',],
                                ['-', 0, '-', 0, '-', 0, '-',],
                                [0, '-', '-', 0, '-', '-', 0,]]
                                )


        #self.tab = np.zeros((7, 7))

        self.a1 = (0,0)
        self.a4 = (3,0)
        self.a7 = (6,0)

        self.b2 = (1,1)
        self.b4 = (3,1)
        self.b6 = (5,1)

        self.c3 = (2,2)
        self.c4 = (3,2)
        self.c5 = (4,2)

        self.d1 = (0,3)
        self.d2 = (1,3)
        self.d3 = (2,3)
        self.d5 = (4,3)
        self.d6 = (5,3)
        self.d7 = (6,3)

        self.e3 = (2,4)
        self.e4 = (3,4)
        self.e5 = (4,4)

        self.f2 = (1,5)
        self.f4 = (3,5)
        self.f6 = (5,5)

        self.g1 = (0,6)
        self.g4 = (3,6)
        self.g7 = (6,6)

        self.actives_cells = [self.a1, self.a4, self.a7, self.b2, self.b4, self.b6, self.c3, self.c4, self.c5, self.d1, self.d2, self.d3, self.d5, self.d6, self.d7, self.e3, self.e4, self.e5, self.f2, self.f4, self.f6, self.g1, self.g4, self.g7]

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
        
        cells = [tuple(cell) for cell in np.argwhere(self._board_state == Color.empty)]
        emptys = []
        for cell in cells:
            if cell in self.actives_cells:
                emptys.append(cell)

        return emptys

    def fill_cell(self, cell: (int, int), color):
        if cell in self.actives_cells and self.is_empty_cell(cell):
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

    def mills(self): 

        AA17 = [self.a1, self.a4, self.a7]
        BB26 = [self.b2, self.b4, self.b6]
        CC35 = [self.c3, self.c4, self.c5]
        DD13 = [self.d1, self.d2, self.d3]
        DD57 = [self.d5, self.d6, self.d7]
        EE35 = [self.e3, self.e4, self.e5]
        FF26 = [self.f2, self.f4, self.f6]
        GG17 = [self.g1, self.g4, self.g7]

        AG11 = [self.a1, self.d1, self.g1]
        BF22 = [self.b2, self.d2, self.f2]
        CE33 = [self.c3, self.d3, self.e3]
        AC44 = [self.a4, self.b4, self.c4]
        EG44 = [self.e4, self.f4, self.g4]
        CE55 = [self.c5, self.d5, self.e5]
        BF66 = [self.b6, self.d6, self.f6]
        AG77 = [self.a7, self.d7, self.g7]

        AC13 = [self.a1, self.b2, self.c3]
        CA57 = [self.c5, self.b6, self.a7]
        GE13 = [self.g1, self.f2, self.e3]
        EG57 = [self.e5, self.f6, self.g7]

        return [AA17, BB26, CC35, DD13, DD57, EE35, FF26, GG17, AG11, BF22, CE33, AC44, EG44, CE55, BF66, AG77, AC13, CA57, GE13, EG57 ]

    def player_mills(self, player):
        p_mills = []
        pieces = self.get_player_pieces_on_board(Color(player))
        mills = self.mills()
        for mill in mills: 
            if mill[0] in pieces and mill[1] in pieces and mill[2] in pieces: 
                p_mills.append(mill)
        return p_mills


    def coordinates(self, name):

        if name == 'a1':return (0,0)
        elif name == 'a4':return (3,0)
        elif name == 'a7':return (6,0)

        elif name == 'b2':return (1,1)
        elif name == 'b4':return (3,1)
        elif name == 'b6':return (5,1)

        elif name == 'c3':return (2,2)
        elif name == 'c4':return (3,2)
        elif name == 'c5':return (4,2)

        elif name == 'd1':return (0,3)
        elif name == 'd2':return (1,3)
        elif name == 'd3':return (2,3)
        elif name == 'd5':return (4,3)
        elif name == 'd6':return (5,3)
        elif name == 'd7':return (6,3)

        elif name == 'e3':return (2,4)
        elif name == 'e4':return (3,4)
        elif name == 'e5':return (4,4)

        elif name == 'f2':return (1,5)
        elif name == 'f4':return (3,5)
        elif name == 'f6':return (5,5)

        elif name == 'g1':return (0,6)
        elif name == 'g4':return (3,6)
        elif name == 'g7':return (6,6)

    def names(self, cell):

        if cell == (0,0):return 'a1'
        elif cell == (3,0):return 'a4'
        elif cell == (6,0):return 'a7'

        elif cell == (1,1):return 'b2'
        elif cell == (3,1):return 'b4'
        elif cell == (5,1):return 'b6'

        elif cell == (2,2):return 'c3'
        elif cell == (3,2):return 'c4'
        elif cell == (4,2):return 'c5'

        elif cell == (0,3):return 'd1'
        elif cell == (1,3):return 'd2'
        elif cell == (2,3):return 'd3'
        elif cell == (4,3):return 'd5'
        elif cell == (5,3):return 'd6'
        elif cell == (6,3):return 'd7'

        elif cell == (2,4):return 'e3'
        elif cell == (3,4):return 'e4'
        elif cell == (4,4):return 'e5'

        elif cell == (1,5):return 'f2'
        elif cell == (3,5):return 'f4'
        elif cell == (5,5):return 'f6'

        elif cell == (0,6):return 'g1'
        elif cell == (3,6):return 'g4'
        elif cell == (6,6):return 'g7'
