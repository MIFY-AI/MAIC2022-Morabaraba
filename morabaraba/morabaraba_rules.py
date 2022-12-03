from core.rules import Rule
from core import Color, board
from morabaraba.morabaraba_action import MorabarabaActionType, MorabarabaAction
from morabaraba.morabaraba_board import MorabarabaBoard
MAX_SCORE = 10

class MorabarabaRules(Rule):

    def __init__(self, players):
        self.players = players
        self.current_player = -1 

    @staticmethod 
    def is_legal_move(state, action, player):  # TODO: Update this function to an more
        # optimized one.
        """Check if an action is a legal move.

        Args:
            state (MorabarabaState): A state object from the yote game.
            action (Action): An action object containing the move.
            player (int): The number of the player making the move.
            rewarding_move (bool, optional): True if the move is a stealing move. Defaults to False.

        Returns:
            bool: True is the move is a legal one and False if else.
        """
        action = action.get_action_as_dict() 
        forbidden_mill = state.player1_forbidden_mill if player == -1 else state.player2_forbidden_mill
        actives_cells = state.get_board().actives_cells
        if state.mill:
            if player == state.get_next_player() == state.get_latest_player():
                if action['action_type'] == MorabarabaActionType.STEAL:
                    opponent_piece =  MorabarabaRules.stealables((player * - 1), state.board)
                    if opponent_piece and action['action']['at'] in actives_cells and action['action']['at'] in opponent_piece:
                        return True
            return False
        else:
            if state.get_next_player() == player:
                if action['action_type'] == MorabarabaActionType.ADD and state.in_hand[player] > 0:
                    empty_cells = state.get_board().get_all_empty_cells()
                    if empty_cells and action['action']['to'] in actives_cells and action['action']['to'] in empty_cells:
                        return True
                elif action['action_type'] == MorabarabaActionType.MOVE:
                    if state.get_board().get_cell_color(action['action']['at']) == Color(player):
                        effective_moves = MorabarabaRules.get_effective_cell_moves(state, action['action']['at'])
                        if effective_moves and action['action']['to'] in actives_cells and action['action']['to'] in effective_moves:
                            if forbidden_mill[0] and forbidden_mill[1] is not None: 
                                player_pieces = []
                                player_pieces = state.get_board().get_player_pieces_on_board(Color(player))
                                player_pieces.append(action['action']['to'])
                                player_pieces.remove(action['action']['at'])
                                mills  = state.get_board().player_mills(player, player_pieces)
                                if MorabarabaRules.is_elmt_in_first_is_in_second(forbidden_mill[1],mills): return False
                                else : return True
                            else : return True
                elif action['action_type'] == MorabarabaActionType.FLY:
                    if state.get_board().get_cell_color(action['action']['at']) == Color(player) and len(state.get_board().get_player_pieces_on_board(Color(player))) <= 3:
                        empty_cells = state.get_board().get_all_empty_cells()
                        if empty_cells and action['action']['to'] in actives_cells and action['action']['to'] in empty_cells:
                            return True
                return False
            return False

    @staticmethod 
    def get_effective_cell_moves(state, cell):
        """Give the effective(Only the possible ones) moves a player can make regarding a piece on the board.

        Args:
            state (MorabarabaState): The current game state.
            cell ((int, int)): The coordinates of the piece on the board.
            player (int): The number of the player making the move.

        Returns:
            List: A list containing all the coordinates where the piece can go.
        """
        board = state.get_board()
        if board.is_cell_on_board(cell):
            possibles_moves = MorabarabaRules.get_rules_possibles_moves(cell, board)
            effective_moves = []
            for move in possibles_moves:
                if board.is_empty_cell(move):
                    effective_moves.append(move)
            return effective_moves 

    @staticmethod #done
    def get_rules_possibles_moves(cell, board):
        """Give all possibles moves for a piece according the game rules (Up, down, left, right, oblique).

        Args:
            cell ((int, int)): The coordinates of the piece on the board.
            board_shape ((int, int)): The board shape.

        Returns:
            List: A list containing all the coordinates where the piece could go.
        """
        if(cell == board.a1):
            return [board.a4, board.b2, board.d1]
        elif(cell == board.a4): 
            return [board.a1, board.a7, board.b4]
        elif(cell == board.a7): 
            return [board.a4, board.b6, board.d7]

        elif(cell == board.b2): 
            return [board.a1, board.b4, board.c3, board.d2]
        elif(cell == board.b4): 
            return [board.a4, board.b2, board.b6, board.c4]
        elif(cell == board.b6): 
            return [board.a7, board.b4, board.d6, board.c5]

        elif(cell == board.c3): 
            return [board.b2, board.c4, board.d3]
        elif(cell == board.c4): 
            return [board.b4, board.c3, board.c5]
        elif(cell == board.c5): 
            return [board.b6, board.c4, board.d5]

        elif(cell == board.d1): 
            return [board.a1, board.d2, board.g1]
        elif(cell == board.d2): 
            return [board.b2, board.d1, board.d3, board.f2]
        elif(cell == board.d3): 
            return [board.c3, board.d2, board.e3]

        elif(cell == board.d5): 
            return [board.c5, board.d6, board.e5]
        elif(cell == board.d6): 
            return [board.b6, board.d5, board.d7, board.f6]
        elif(cell == board.d7): 
            return [board.a7, board.d6, board.g7]

        elif(cell == board.e3): 
            return [board.d3, board.f2, board.e4]
        elif(cell == board.e4): 
            return [board.e3, board.f4, board.e5]
        elif(cell == board.e5): 
            return [board.d5, board.e4, board.f6]

        elif(cell == board.f2): 
            return [board.d2, board.e3, board.f4, board.g1]
        elif(cell == board.f4): 
            return [board.e4, board.f2, board.f6, board.g4]
        elif(cell == board.f6): 
            return [board.d6, board.e5, board.f4, board.g7]

        elif(cell == board.g1): 
            return [board.d1, board.f2, board.g4]
        elif(cell == board.g4): 
            return [board.f4, board.g1, board.g7]
        elif(cell == board.g7): 
            return [board.d7, board.f6, board.g4]

    @staticmethod 
    def make_move(state, action, player):  
        """Transform the action of the player to a move. The move is made and the reward computed. 

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
            action (Action): An action object containing the move.Morabaraba
            player (int): The number of the player making the move.
            mill (bool, optional): True if the move is a stealing move. Defaults to False.

        Returns: (next_state, done, next_is_reward): Gives the next state of the game along with the game status and
        the type of the next step.
        """
        board = state.get_board()
        json_action = action.get_json_action()
        action = action.get_action_as_dict()
        captured = None
        is_mill = False
        reward = 0

        if state.mill:
            state.boring_moves = 0
            if action['action_type'] == MorabarabaActionType.STEAL:
                at = action['action']['at']
                captured = at
                board.empty_cell(at)
                #board.tab[at] = '0'
                is_mill = False
                reward += 1
        else:
            if action['action_type'] == MorabarabaActionType.ADD:
                state.boring_moves += 1
                state.in_hand[player] -= 1
                board.fill_cell(action['action']['to'], Color(player))
                #if player == -1: board.tab[action['action']['to']] = '1'
                #else: board.tab[action['action']['to']] = '2'
                is_mill = MorabarabaRules.is_making_mill(board, player, action['action']['to'])[0]
            elif action['action_type'] == MorabarabaActionType.MOVE:
                state.boring_moves += 1 
                before_move_mills = board.player_mills(player)             
                at = action['action']['at']
                to = action['action']['to']
                board.empty_cell(at)
                #board.tab[at] = '0'
                board.fill_cell(to, Color(player))
                after_move_mills = board.player_mills(player)   
                #if player == -1: board.tab[to] = '1'
                #else: board.tab[to] = '2'
                is_mill = MorabarabaRules.is_making_mill(board, player, action['action']['to'])[0]
                issue = [item for item in before_move_mills if item not in after_move_mills]
                if len(issue) > 0:
                    if player == -1:                 
                        state.player1_forbidden_mill = [True, issue]
                    else: 
                        state.player2_forbidden_mill = [True, issue]
                else:
                    if player == -1:                 
                        state.player1_forbidden_mill = [False, None]
                    else: 
                        state.player2_forbidden_mill = [False, None]
            elif action['action_type'] == MorabarabaActionType.FLY:
                state.boring_moves += 1
                before_move_mills = board.player_mills(player)  
                at = action['action']['at']
                to = action['action']['to']
                board.empty_cell(at)
                #board.tab[at] = '0'
                board.fill_cell(to, Color(player))
                after_move_mills = board.player_mills(player)  
                #if player == -1: board.tab[to] = '1'
                #else: board.tab[to] = '2'
                is_mill = MorabarabaRules.is_making_mill(board, player, action['action']['to'])[0]
                issue = [item for item in before_move_mills if item not in after_move_mills]
                if len(issue) > 0:
                    if player == -1:                 
                        state.player1_forbidden_mill = [True, issue]
                    else: 
                        state.player2_forbidden_mill = [True, issue]
                else:
                    if player == -1:                 
                        state.player1_forbidden_mill = [False, None]
                    else: 
                        state.player2_forbidden_mill = [False, None]
        state.set_board(board)
        state.score[player] += reward
        state.captured = captured
        state.mill = is_mill
        state.set_latest_player(player)
        state.set_latest_move(json_action)
        
        
        if is_mill:
            state.set_next_player(player)
        else:
            state.set_next_player(player * -1)

        if state.fly_case:
            if is_mill: state.fly_moves == 0
            else : state.fly_moves += 1

        done = MorabarabaRules.is_end_game(state)
        return state, done, is_mill

    @staticmethod
    def is_making_mill(board, player, cell): 
        """Take the board, the player and his action and find a mill.

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
            action (Action): An action object containing the move.
            player (int): The number of the player making the move.

        Returns:
            bool: True if everything goes fine and the move was made. False is else.
        """
        player_mills = []
        pieces = board.get_player_pieces_on_board(Color(player))
        mills = board.mills()
        for mill in mills:
            if cell in mill: 
                is_mill = True
                for mill_cell in mill:
                    if mill_cell not in pieces : is_mill =  False   
                if is_mill == True: 
                    player_mills.append(mill)
                
        if len(player_mills) == 0: is_player_mill = False 
        else : is_player_mill = True 
        
        return [ is_player_mill , player_mills ]


    @staticmethod
    def act(state, action, player): 
        """Take the state and the player's action and make the move if possible.

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
            action (Action): An action object containing the move.
            player (int): The number of the player making the move.

        Returns:
            bool: True if everything goes fine and the move was made. False is else.
        """
        if MorabarabaRules.is_legal_move(state, action, player):
            return MorabarabaRules.make_move(state, action, player)
        else:
            return False



    @staticmethod 
    def get_player_actions(state, player):
        """Provide for a player and at a state all of his possible actions.

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
            player (int): The number of the player making the move.
            reward_move (bool, optional): True if the move is a stealing move. Defaults to False.

        Returns:
            List[MorabarabaAction]: Contains all possible actions for a player at the given state.
        """
        actions = []
        board = state.get_board()
        empty_cells = board.get_all_empty_cells()
        stealables = MorabarabaRules.stealables((player * -1), board)
        player_pieces = board.get_player_pieces_on_board(Color(player))
        if state.mill:
            for piece in stealables:
                actions.append(MorabarabaAction(action_type=MorabarabaActionType.STEAL, at=piece))
            return actions
        else: 
            if state.in_hand[player] > 0 :
                if empty_cells:
                    for cell in empty_cells:
                        actions.append(MorabarabaAction(action_type=MorabarabaActionType.ADD, to=cell))
                return actions
            elif state.in_hand[player] == 0:
                player_pieces = board.get_player_pieces_on_board(Color(player))
                if len(player_pieces) > 3:
                    for piece in player_pieces:
                        moves = MorabarabaRules.get_effective_cell_moves(state, piece)
                        if moves:
                            for move in moves:
                                forbidden_mill = state.player1_forbidden_mill if player == -1 else state.player2_forbidden_mill

                                if forbidden_mill[0]: 
                                    if forbidden_mill[1] is not None :
                                        player_pieces = []
                                        player_pieces = board.get_player_pieces_on_board(Color(player))
                                        player_pieces.append(move)
                                        player_pieces.remove(piece)
                                        mills  = board.player_mills(player, player_pieces)
                                        if not MorabarabaRules.is_elmt_in_first_is_in_second(forbidden_mill[1],mills):
                                            actions.append(MorabarabaAction(action_type=MorabarabaActionType.MOVE, at=piece, to=move))
                                else : 
                                    actions.append(MorabarabaAction(action_type=MorabarabaActionType.MOVE, at=piece, to=move))
                else:
                    state.fly_case = True 
                    for piece in player_pieces:
                        moves = empty_cells
                        if moves:
                            for move in moves:
                                forbidden_mill = state.player1_forbidden_mill if player == -1 else state.player2_forbidden_mill

                                if forbidden_mill[0]: 
                                    if forbidden_mill[1] is not None :
                                        player_pieces = []
                                        player_pieces = board.get_player_pieces_on_board(Color(player))
                                        player_pieces.append(move)
                                        player_pieces.remove(piece)
                                        mills  = board.player_mills(player, player_pieces)
                                        if not MorabarabaRules.is_elmt_in_first_is_in_second(forbidden_mill[1],mills):
                                            actions.append(MorabarabaAction(action_type=MorabarabaActionType.FLY, at=piece, to=move))
                                else : 
                                    actions.append(MorabarabaAction(action_type=MorabarabaActionType.FLY, at=piece, to=move))
                return actions

                
    @staticmethod
    def stealables(player, board): 
        pieces = board.get_player_pieces_on_board(Color(player))
        mills = board.player_mills(player)
        actives_cells  = board.actives_cells
        mills_pieces = [] 
        for mill in mills: 
            for cell in mill:
                if cell in actives_cells:
                    if not cell in mills_pieces : mills_pieces.append(cell)
        if len(mills_pieces) > 0: 
            for cell in mills_pieces: 
                if cell in pieces : pieces.remove(cell)
        if len(pieces) == 0: 
            return mills_pieces
        else : 
            return pieces


    @staticmethod
    def moment_player(state):
        player = state.get_next_player() 
        return player 

    @staticmethod
    def is_elmt_in_first_is_in_second(first, second):
        right = False
        for elmt in first: 
            if elmt in second :
                right = True
        return right

    @staticmethod
    def random_play(state, player):
        """Return a random move for a player at a given state.

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
            player (int): The number of the player making the move.

        Returns:
            action : An action
        """
        import random
        actions = MorabarabaRules.get_player_actions(state, player)
        if len(actions) == 0:
            choice = None
        else:
            choice = random.choice(actions)
        return choice

    @staticmethod 
    def is_player_stuck(state, player):
        """Check if a player has the possibility to make a move

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
            player (int): The number of the player making the move.

        Returns:
            bool: True if a player can make a move. False if not.
        """
        #if state.mill is None: 
        return len(MorabarabaRules.get_player_actions(state, player)) == 0

    @staticmethod
    def is_end_game(state): 
        """Check if the given state is the last one for the current game.

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.

        Returns:
            bool: True if the given state is the final. False if not.
        """
        if MorabarabaRules.is_player_stuck(state, state.get_next_player()) or MorabarabaRules.is_boring(state) : #
            return True
        if state.in_hand[state.get_latest_player()] == 0 or state.in_hand[(state.get_latest_player() * -1)] == 0:
            if len(state.get_board().get_player_pieces_on_board(Color(state.get_latest_player() * -1))) == 2 or len(state.get_board().get_player_pieces_on_board(Color(state.get_latest_player()))) == 2 : 
                return True
        if state.fly_moves == 10:
            return True
        latest_player_score = state.score[state.get_latest_player()]
        if latest_player_score >= MAX_SCORE:
            return True
        return False

    @staticmethod
    def is_boring(state):
        """Check if the game is ongoing without winning moves

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.
        Returns:
            bool: True if the game is boring. False if else.
        """
        return state.boring_moves >= state.just_stop

    @staticmethod
    def get_results(state):  # TODO: Add equality case. a voir
        """Provide the results at the end of the game.

        Args:
            state (MorabarabaState): A state object from the Morabaraba game.

        Returns:
            Dictionary: Containing the winner and the game score.
        """
        tie = False
        if state.score[-1] == state.score[1]:
            tie = True

        return {'tie': tie,  'winner': max(state.score, key=state.score.get),
                'score': state.score}