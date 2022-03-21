# Author: Joseph Coiffman
# Date: 11/27/2020
# Description: I already initialized the board.
# The first thing the make move will do is check whose turn it is,
# if it is false it will return the statement for wrong turn it is.
# then it will check the top of the stack at that position to see if it is a valid move
# and checks to make sure not diagonal
# will update the board and then update capture and reserve and then check to see if anyone won
# the self._capture_and_reserved will be checked by using the get_captured_and_reserved.
# The position translates perfectly to board, board[position[0][position[1] is an easy way to use it,
# and easy to check the length and to see the top piece.
# To get the name of the player, I will use self_player1[0] and self._player2[0], and color would be [1]
#


class FocusGame:
    """The board will be a list of lists, 6 X 6, each position will contain the players tuple of the piece that is there
    including multiple tuples when there are more then one piece"""
    def __init__(self, _player1, _player2):
        self._player1 = _player1
        self._player2 = _player2
        self._board = [[['R'], ['R'], ['G'], ['G'], ['R'], ['R']],
                      [['G'], ['G'], ['R'], ['R'], ['G'], ['G']],
                      [['R'], ['R'], ['G'], ['G'], ['R'], ['R']],
                      [['G'], ['G'], ['R'], ['R'], ['G'], ['G']],
                      [['R'], ['R'], ['G'], ['G'], ['R'], ['R']],
                      [['G'], ['G'], ['R'], ['R'], ['G'], ['G']]]
        self._captured_and_reserved = [[self._player1[0], [], []], [self._player2[0], [], []]]
        self._player_turn = None

    def move_piece(self, player_name, move_from, move_to, number_of_pieces):
        """will take the list of move_from, check_turn, to see if True or False, check top_of_stack to match with player,
        And iterate make sure the move_to is at least equal to either the row or the column that the move_to is equal to
        then checks the number of pieces to move, upend it to move_to, and update move_from,
         update capture_or_reserve and check win, by using check_win"""
        pass

    def top_of_stack(self, position):
        """returns the piece that is on top of the stack by using board[position[0]][position[1][-1]"""
        pass

    def change_turn(self, player_name):
        """if self._player_turn is none then initialize it to player name.
         If payer name equals player_turn, changes player turn to the next player, the other players name
          and returns True.
        Otherwise returns False."""
        pass

    def check_win(self):
        """ will check capture for each player and see if someone won"""
        pass

    def capture_or_reserve(self, player_name, move_to, number_of_pieces):
        """Will check the move, and check how many pieces there are in that place, if more then 5
        Will update self.captured_and_reserved,
        list [0] with playerA's captured (at [1]) and reserved (at [2]) pieces, and list [1] with playerB's """
        pass

    def get_captured_and_reserved(self):
        return self._captured_and_reserved


    def show_pieces(self, position):
        """takes the position and shows the color of the pieces starting with the bottom most"""
        pass

    def show_reserve(self, player_name):
        """Takes player_name, and goes through get_captured_and_reserved, returns the players reserved,
         the list starts with the players name and reserved is the second list"""
        pass

    def show_captured(self, players_name):
        """Takes player_name, and goes through get_captured_and_reserved, returns the players reserved,
                 the list starts with the players name and captured is the first list"""

    def reserved_move(self, player_name, location):
        """takes player's name and checks if the have pieces reserved by using get_captured_and_reserved,
        then checks change_turn, decrements reserved for that player.And adds another piece to the list at location."""
        pass
