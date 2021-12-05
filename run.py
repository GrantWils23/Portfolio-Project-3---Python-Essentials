# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

scores = {"computer": 0}


class CustomError(Exception):
    """
    This error is raised when the guesses list is being check against the
    new given guess coordinates
    """


class GameBoard():
    """
    This is the model for the game board class. Here inside the Game_Board
    Class you can set the size of the board, the number of ships, the board
    player (computer or user)
    """
    def __init__(self, size, num_of_ships, player_type, player_name):
        self.size = size
        self.board_grid = [["." for x in range(size)] for y in range(size)]
        self.num_of_ships = num_of_ships
        self.player_type = player_type
        self.player_name = player_name
        self.guesses = []
        self.ships = []

    def display_board(self):
        for row in self.board_grid:
            print("  ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board_grid[x][y] = "X"

        if (x, y) in self.ships:
            self.board_grid[x][y] = "@"
            return "Hit"
        else:
            return "Miss"

    def display_ships(self):
        for co_ord in self.ships:
            x, y = co_ord
            if self.player_type == "user":
                self.board_grid[x][y] = "$"


def random_number(boardsize):
    """
    helper function that creates a random interger based on the boardsize
    """
    return int(random.randint(0, boardsize - 1))


def add_ships_to_board(gameboard):
    """
    This function generates the random location of ships to the board. it takes the
    players_board and computers_board as the arguments
    """
    num_of_ships = gameboard.num_of_ships
    ship_list = []
    unique_coordinates = []

    while len(unique_coordinates) < num_of_ships:
        x = random_number(gameboard.size)
        y = random_number(gameboard.size)
        ship = (x, y)
        ship_list.append(ship)
        unique_coordinates = set(ship_list)
        gameboard.ships = list(unique_coordinates)
        gameboard.display_ships()

    # print(ship_list)
    # print(unique_coordinates)


def input_coordinate(boardsize, row_or_column):
    """
    input a coordinate
    """
    num = int(input(f'Enter a number between 0 and {boardsize - 1} for the {row_or_column}:  '))
    return num


def make_guess(gameboard, x, y):
    """
    prompt the user to make a guess that is stored in the player.guesses list
    """
    return gameboard.guess(x, y)


def validate_input(gameboard, row_or_column):
    """
    Validate the input co-ordinate given to make sure that it is not a string.
    """
    while True:
        try:
            num = input_coordinate(gameboard.size, row_or_column)
            return int(num)
        except ValueError as error:
            e = str(error).split()
            print(f'{e[-1]} is not a number')

##################################################################

#################################################################


def validate_input_coordinates(gameboard):
    """
    Checks to validate if the given x and y coirdinates are
     in range of the boardsize. returns the called make guess function
     and unpacks the x, y co-ordinates that were fed into the guess.
    """
    while True:
        try:
            if gameboard.player_type == "computer":
                x = validate_input(gameboard, "row")
                y = validate_input(gameboard, "column")
                if (x, y) in gameboard.guesses:
                    raise CustomError
            else:
                x = int(random_number(gameboard.size))
                y = int(random_number(gameboard.size))
                if (x, y) in gameboard.guesses:
                    raise CustomError
            return make_guess(gameboard, x, y), x, y
        except IndexError:
            print(f" Index values provided are out of range, please select numbers between 0 and {gameboard.size - 1}")
        except CustomError:
            if gameboard.player_type == "computer":
                print("please select a co-ordinate that hasn't already been chosen")
                

################################################################


def calculate_score(turn, gameboard):
    """
    calculates the score after feeding it the turn and the board as parameters
    """
    if turn == "Hit":
        if gameboard.player_type == "user":
            scores[gameboard.player_name] += 1
            return scores
        else:
            scores["computer"] += 1
            return scores

################################################################


def playgame(players_board, computers_board):
    """
     this function takes the player and the computer players as parameters
     and calls the functions to make guesses in the game until there is a winner
     """
    while scores["computer"] or scores[players_board.player_name] <= 4:
        print(f"{players_board.player_name}. It is your turn to attack!")
        print("Prepare to enter the grid co-ordinates to strike.")
        print("-" * 65)
        players_turn, x, y = validate_input_coordinates(computers_board)
        print("-" * 65)
        print(f"Shot fired!, target '{players_turn}' at co-ordinates{(x, y)}")
        print("-" * 65)
        print(f"It's now the {computers_board.player_name}'s turn to attack.")
        computers_turn, x, y = validate_input_coordinates(players_board)
        print(f"Shot fired!, target '{computers_turn}' at co-ordinates{(x, y)}")
        print()

        print(f"{players_board.player_name}'s Battleship Board")
        print("-" * 40)
        players_board.display_board()
        print(f"{computers_board.player_name}'s Battleship Board")
        print("-" * 40)
        computers_board.display_board()
        print()

        calculate_score(players_turn, players_board)
        calculate_score(computers_turn, computers_board)
        print("The scores at the end of the round are:")
        print(scores)
        print()
        if (scores[players_board.player_name] == 4) or (scores["computer"] == 4):
            break
    if scores[players_board.player_name] == 4:
        print(f"Congratulations {players_board.player_name}! You won!")
    else:
        print("Unlucky, The computer beat you this time!")

    play_again = str(input("Would you like to play again? press any key to continue or 'n' to quit: \n"))
    if play_again != "n":
        scores.pop(players_board.player_name)
        start_game()
    


#------------------------------------------------------------------------------------------------------

    # print(f"{players_board.player_name}. It is your turn to attack!")
    # print("Prepare to enter the grid co-ordinates to strike.")
    # print("-" * 65)
    # players_turn, x, y = validate_input_coordinates(computers_board)
    # print("-" * 65)
    # print(f"Shot fired!, target '{players_turn}' at co-ordinates{(x, y)}")
    # print("-" * 65)
    # print(f"It's now the {computers_board.player_name}'s turn to attack.")
    # rand_x = int(random_number(players_board.size))
    # rand_y = int(random_number(players_board.size))
    # computers_turn = make_guess(players_board, rand_x, rand_y)
    # print(f"Shot fired!, target '{computers_turn}' at co-ordinates{(x, y)}")
    # print()


    # print(f"{players_board.player_name}'s Battleship Board")
    # print("-" * 40)
    # print()
    # players_board.display_board()
    # print()
    # print(f"{computers_board.player_name}'s Battleship Board")
    # print()
    # print("-" * 40)
    # computers_board.display_board()
    # print()

    # calculate_score(players_turn, players_board)
    # calculate_score(computers_turn, computers_board)
    # print("The scores at the end of the round are:")
    # print(scores)
    # print()

#--------------------------------------------------------------------------------------------------------------------------------------

def start_game():
    """
    runs the game and instatiates all the variables required to run the game
    """

    board_size = 5
    num_of_ships = 4
    players_name = input("What is your name? \n")
    scores["computer"] = 0
    scores[players_name] = 0
    players_board = GameBoard(board_size, num_of_ships, player_type="user", player_name=players_name)
    computers_board = GameBoard(board_size, num_of_ships, player_type="computer", player_name="Computer")

    print()
    print("*" * 40)
    print("Welcome to the BattleShips board!")
    print(f"The Boardsize: {board_size}, The number of ships: {num_of_ships}")
    print("The top left grid co-ordinate is (0, 0)")
    print("*" * 40)

    add_ships_to_board(players_board)
    add_ships_to_board(computers_board)

    print()
    print(f"{players_board.player_name}'s Battleship Board")
    print("-" * 40)
    print()
    players_board.display_board()
    print()
    print(f"{computers_board.player_name}'s Battleship Board")
    print("-" * 40)
    computers_board.display_board()
    print()

    playgame(players_board, computers_board)


print()
print("-" * 65)
print("Welcome to the BATTLESHIPS! This is turn-based stratergy game")
print("were the players take turns guessing co-ordinates on a grid to")
print("shoot and take out your opponents ships before they take out")
print("yours. The first one to take out all of each others ships wins!")
print("-" * 65)
print()
start_game()
