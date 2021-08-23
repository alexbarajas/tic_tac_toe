import math
import random


class Player():
    def __init__(self, letter):
        # the letter will either be an "x" or an "o"
        self.letter = letter

    # where the next move will be given to the player
    def get_move(self, game):
        pass


class Human(Player):  # inherits from the Player super class
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid space for the next move
        valid_square = False
        value = None
        while not valid_square:
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say it's invalid
            # if that spot is not available on the board, we also say it's invalid
            square = input(self.letter + "\'s turn. Input move (0-9): ")
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True  # if the value exists in the available spaces
            except ValueError:
                print("Invalid square. Try again.")
        return value


class Computer(Player):  # inherits from the Player super class
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid space for the next move
        square = random.choice(game.available_moves())
        return square


class AI(Player):  # inherits from the Player super class
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid space for the next move
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # randomly chooses a spot
        else:  # gets the square based off the minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = "O" if player == "X" else "X"

        # first we want to check if the previous move is a winner
        # this is the base case
        if state.current_winner == other_player:
            # we should return position and score because we need to keep track of the score for minimax to work
            return {"position": None,
                    "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                            state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # each score should maximize
        else:
            best = {"position": None, "score": math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move by alternating players

            # step 3: undo move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move  # this represents the move optimal next move

            # step 4: update the dictionaries if necessary
            if player == max_player:  # X is max player
                if sim_score["score"] > best["score"]:
                    best = sim_score  # replaces the best score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score  # replaces the best score
        return best
