import json

class MorabarabaState(object):  # TODO: Link it to the core state.

    def __init__(self, board, next_player=-1, boring_limit=50):
        """The State of the Morabaraba Game. It contains information regarding the game such as:
            - board          : The current board
            - score          : The game score
            - on_board       : The number of piece on the board for each player
            - latest_move    : The latest performed action
            - latest_player  : The latest player
            - next_player    : The next player
            - rewarding_move : True if the next move is a stealing. False if not.
                **********
            - just_stop      : The limit of non rewarding moves
            - boring_moves   : The current number of non rewarding moves
           
        Args:
            board (Board): The board game
            next_player (int, optional): The next or first play at the start. Defaults to -1.
            boring_limit (int, optional): Limit of non rewarding moves. Defaults to 200.
        """

        self.board = board
        self._latest_player = None
        self._latest_move = None
        self._next_player = next_player
        self.score = {-1: 0, 1: 0}
        #self.on_board = {-1: 22, 1: 22}
        self.in_hand = {-1: 12, 1: 12}
        self.mill = False
        self.fly_case = False
        self.boring_moves = 0
        self.just_stop = boring_limit
        self.captured = None
        self.player1_forbidden_mill = [False, None]
        self.player2_forbidden_mill = [False, None]
        self.fly_moves = 0

    def get_board(self):
        return self.board

    def set_board(self, new_board):
        self.board = new_board

    def get_latest_player(self):
        return self._latest_player

    def get_latest_move(self):
        return self._latest_move

    def get_next_player(self):
        return self._next_player

    def set_latest_move(self, action):
        self._latest_move = action

    def set_next_player(self, player):
        self._next_player = player

    def set_latest_player(self, player):
        self._latest_player = player

    def get_player_info(self, player):
        return {'in_hand': self.in_hand[player],
                'on_board': 12 - self.in_hand[player] - self.score[(-1*player)],
                'score': self.score[player]}

    def get_json_state(self):
        json_state = {'latest_player': self.get_latest_player(),
                      'latest_move': self.get_latest_move(),
                      'next_player': self.get_next_player(),
                      'score': self.score,
                      'in_hand': self.in_hand,
                      'rewarding_move': self.mill,
                      'boring_moves': self.boring_moves,
                      'just_stop': self.just_stop,
                      'board': self.board.get_json_board(),
                      }
        return json.dumps(json_state, default=str)
