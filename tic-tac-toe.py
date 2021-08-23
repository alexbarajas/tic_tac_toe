import math
import time
from player import Human, Computer, AI


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None  # keeps track of the winner

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def make_move(self, square, letter):
        # if valid move, then make the move by assigning a square to a letter
        # then return True. if invalid, return False
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere. we have to check every scenario
        # check the rows
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        # print("row", row)
        if all([s == letter for s in row]):
            return True
        # check the columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        # print("col", column)
        if all([s == letter for s in column]):
            return True
        # check the diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([s == letter for s in diagonal2]):
                return True
        # if all of these checks fail return False
        return False

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
        # moves = []  # same as the line above
        # for (i, space) in enumerate(self.board):
        #     # ["x", "x", "o"] --> [(0, "x"), (1, "x"), (2, "o")]
        #     if space == "":
        #         moves.append(i)
        # return moves


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter)! or None for a tie

    if print_game:
        game.print_board_nums()

    letter = "X"  # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about the winner because
    # we'll just return that which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # let's define a function to make a move
        if game.make_move(square, letter):

            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter  # ends the loop and exits the game

            # after we made our move, we need to alternate letters
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
            # letter = "O" if letter == "X" else "X"   # this switches the player, same as the if statement above

        time.sleep(.8)

    if print_game:
        print("It\'s a tie!")


# if __name__ == '__main__':
#     x_player = AI('X')
#     o_player = Human('O')
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game=True)


x_player = AI("X")
o_player = Human("O")
t = TicTacToe()
play(t, x_player, o_player, print_game=True)
