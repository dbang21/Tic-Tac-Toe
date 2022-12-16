# Author: Dionne Bang
# Date: 12/7/22
# Description: Classes for TicTacToe game.

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.tictactoe_x = ['X', 'X', 'X']
        self.tictactoe_o = ['O', 'O', 'O']
        self.game_state = 'UNFINISHED'
        self.active_player = 'X'
        self.game_result = None
        self.move_validity = True
        self.squares = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    def print_board(self):
        """Prints the current board."""
        columns = ['1', '2', '3']
        print(' ', *columns)
        print('A', *self.board.board[0])
        print('B', *self.board.board[1])
        print('C', *self.board.board[2])

    def get_move_validity(self):
        """Returns the current state of the game."""
        return self.move_validity

    def set_move_validity(self, validity):
        """ sets the current state of the game. """
        self.move_validity = validity

    def get_game_state(self):
        """Returns the current state of the game."""
        return self.game_state

    def set_game_state(self, state):
        """ sets the current state of the game. """
        self.game_state = state

    def get_game_result(self):
        """Returns the current state of the game."""
        return self.game_result

    def set_game_result(self, result):
        """ sets the current state of the game. """
        self.game_result = result

    def get_active_player(self):
        """Returns whose turn it is."""
        return self.active_player

    def set_active_player(self, player):
        """ sets new active player. """
        self.active_player = player

    def make_move(self, move):
        if self.get_game_state() == 'UNFINISHED':
            square = move
            square = square.upper()
            if square in self.squares and self.if_empty(square, self.active_player) != False:
                # if client side
                if self.active_player == 'X':
                    self.if_empty(square, 'X')
                    self.set_move_validity(True)
                    # if winning move
                    for x in self.board.winning_opts:
                        if x == self.tictactoe_x:
                            self.set_game_result('X wins!')
                            self.set_game_state('GAME OVER')
                            self.set_active_player('O')
                            self.print_board()
                            print(self.get_game_result())
                            return
                    self.set_active_player('O')

                    # check if draw
                    for y in self.board.board:
                        if '-' in y:
                            self.print_board()
                            return
                    self.set_game_result('It\'s a draw!')
                    self.set_game_state('GAME OVER')
                    self.print_board()
                    return
                # if server side
                else:
                    self.if_empty(square, 'O')
                    self.set_move_validity(True)
                    # if winning move
                    for x in self.board.winning_opts:
                        if x == self.tictactoe_o:
                            self.set_game_result('O wins!')
                            self.set_game_state('GAME OVER')
                            self.set_active_player('X')
                            self.print_board()
                            print(self.get_game_result())
                            return
                    self.set_active_player('X')

                    # check if draw
                    for y in self.board.board:
                        if '-' in y:
                            self.print_board()
                            return
                    self.set_game_result('It\'s a draw!')
                    self.set_game_state('GAME OVER')
                    self.print_board()
                    return
            elif square not in self.squares or not self.if_empty(square, self.active_player):
                print('Invalid move.')
                self.set_move_validity(False)
                return

        else:
            print(self.get_game_state())
            return

    def if_empty(self, square, player):
        if player == 'X':
            if square == 'A1' and self.board.row1[0] == '-':
                self.board.row1[0] = 'X'
                self.board.column1[0] = 'X'
                self.board.diagonal_l[0] = 'X'
                return
            elif square == 'A2' and self.board.row1[1] == '-':
                self.board.row1[1] = 'X'
                self.board.column2[0] = 'X'
                return
            elif square == 'A3' and self.board.row1[2] == '-':
                self.board.row1[2] = 'X'
                self.board.column3[0] = 'X'
                self.board.diagonal_r[0] = 'X'
                return
            elif square == 'B1' and self.board.row2[0] == '-':
                self.board.row2[0] = 'X'
                self.board.column1[1] = 'X'
                return
            elif square == 'B2' and self.board.row2[1] == '-':
                self.board.row2[1] = 'X'
                self.board.column2[1] = 'X'
                self.board.diagonal_l[1] = 'X'
                self.board.diagonal_r[1] = 'X'
                return
            elif square == 'B3' and self.board.row2[2] == '-':
                self.board.row2[2] = 'X'
                self.board.column3[1] = 'X'
                return
            elif square == 'C1' and self.board.row3[0] == '-':
                self.board.row3[0] = 'X'
                self.board.column1[2] = 'X'
                self.board.diagonal_r[2] = 'X'
                return
            elif square == 'C2' and self.board.row3[1] == '-':
                self.board.row3[1] = 'X'
                self.board.column2[2] = 'X'
                return
            elif square == 'C3' and self.board.row3[2] == '-':
                self.board.row3[2] = 'X'
                self.board.column3[2] = 'X'
                self.board.diagonal_l[2] = 'X'
                return
            else:
                return False

        else:
            if square == 'A1' and self.board.row1[0] == '-':
                self.board.row1[0] = 'O'
                self.board.column1[0] = 'O'
                self.board.diagonal_l[0] = 'O'
                return
            elif square == 'A2' and self.board.row1[1] == '-':
                self.board.row1[1] = 'O'
                self.board.column2[0] = 'O'
                return
            elif square == 'A3' and self.board.row1[2] == '-':
                self.board.row1[2] = 'O'
                self.board.column3[0] = 'O'
                self.board.diagonal_r[0] = 'O'
                return
            elif square == 'B1' and self.board.row2[0] == '-':
                self.board.row2[0] = 'O'
                self.board.column1[1] = 'O'
                return
            elif square == 'B2' and self.board.row2[1] == '-':
                self.board.row2[1] = 'O'
                self.board.column2[1] = 'O'
                self.board.diagonal_l[1] = 'O'
                self.board.diagonal_r[1] = 'O'
                return
            elif square == 'B3' and self.board.row2[2] == '-':
                self.board.row2[2] = 'O'
                self.board.column3[1] = 'O'
                return
            elif square == 'C1' and self.board.row3[0] == '-':
                self.board.row3[0] = 'O'
                self.board.column1[2] = 'O'
                self.board.diagonal_r[2] = 'O'
                return
            elif square == 'C2' and self.board.row3[1] == '-':
                self.board.row3[1] = 'O'
                self.board.column2[2] = 'O'
                return
            elif square == 'C3' and self.board.row3[2] == '-':
                self.board.row3[2] = 'O'
                self.board.column3[2] = 'O'
                self.board.diagonal_l[2] = 'O'
                return
            else:
                return False


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.row1 = self.board[0]
        self.row2 = self.board[1]
        self.row3 = self.board[2]
        self.column1 = [self.board[0][0], self.board[1][0], self.board[2][0]]
        self.column2 = [self.board[0][1], self.board[1][1], self.board[2][1]]
        self.column3 = [self.board[0][2], self.board[1][2], self.board[2][2]]
        self.diagonal_l = [self.board[0][0], self.board[1][1], self.board[2][2]]
        self.diagonal_r = [self.board[0][2], self.board[1][1], self.board[2][0]]
        self.winning_opts = [self.row1, self.row2, self.row3, self.column1, self.column2, self.column3, self.diagonal_l,
                             self.diagonal_r]
