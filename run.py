# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from os import sched_setscheduler, strerror
import random

scores = {"player": 0, "computer": 0}

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
        # if len(self.player.ships) > self.num_of_ships:
        #     print("Error: you cannot add anymore ships to the board")
        # else:
        for co_ord in self.ships:
            x, y = co_ord
            if self.player_type == "user":
                self.board_grid[x][y] = "$"


def random_number(boardsize):
    """
    helper function that creates a random interger based on the boardsize
    """
    return int(random.randint(0, boardsize - 1))


def add_ships_to_board(GameBoard):
    """
    This function generates the random location of ships to the board. it takes the
    players_board and computers_board as the arguments
    """
    num_of_ships = GameBoard.num_of_ships
    ship_list = []
    unique_coordinates = []

    while len(unique_coordinates) < num_of_ships:
        x = random_number(GameBoard.size)
        y = random_number(GameBoard.size)
        ship = (x, y)
        # print(ship) # program checker print
        ship_list.append(ship)
        unique_coordinates = set(ship_list)
        GameBoard.ships = list(unique_coordinates)
        GameBoard.display_ships()

    print(ship_list)
    print(unique_coordinates)



def make_guess(GameBoard):
    """
    prompt the user to make a guess that is stored in the player.guesses list
    """
    if GameBoard.player_type == "user":
        print("please enter the coordinates you would like to strike")
        x = input_coordinate(GameBoard.size, "X co-ordinate")
        y = input_coordinate(GameBoard.size, "Y co-ordinate")
        GameBoard.guess(x, y)
    else:
        x = random_number(GameBoard.size)
        y = random_number(GameBoard.size)
        GameBoard.guess(x, y)


def playgame(players_board, computers_board):
    """
     this function takes the player and the computer players as parameters
     and calls the functions to make guesses in the game until there is a winner
     """
    make_guess(players_board)
    make_guess(computers_board)
    print()
    print(f"{players_board.player_name}'s Battleship Board")
    print("-" * 40)
    print()
    players_board.display_board()
    print(f"{computers_board.player_name}'s Battleship Board")
    print("-" * 40)
    computers_board.display_board()
    print()

#--------------------------------------------------------------------------------------------------------------------------------------

def input_coordinate(boardsize, row_or_column):
    """
    input a coordinate 
    """
    num = int(input(f'Enter a number between 0 and {boardsize - 1} for the {row_or_column}: \n'))
    return num





def start_game():
    """
    runs the game and instatiates all the variables required to run the game
    """
    board_size = 5
    num_of_ships = 4
    players_name = input("What is your name? \n")
    players_board = GameBoard(board_size, num_of_ships, player_type="user", player_name=players_name)
    computers_board = GameBoard(board_size, num_of_ships, player_type="computer", player_name="Computer")

    add_ships_to_board(players_board)
    add_ships_to_board(computers_board)

    print()
    print(f"{players_board.player_name}'s Battleship Board")
    print("-" * 40)
    print()
    players_board.display_board()
    print(f"{computers_board.player_name}'s Battleship Board")
    print("-" * 40)
    computers_board.display_board()
    print()

    playgame(players_board, computers_board)

start_game()

#------------------------------------------------------------------------------------------------------------------

# def validate_coordinate(boardsize, row_or_column):
#     """
#     Validate the co-ordinates given that they are not a string.
#     """
#     while True:
#         try:
#             num = input(f'Enter a number between 0 and {boardsize} for the {row_or_column}: \n')
#             # if num >= boardsize:
#                 # print(f" Index values provided are out of range, please select a number between 0 and {boardsize - 1}")
#             print(f'Number is {num}')
#             return int(num)
#         except ValueError:
#             print(f'{num} is not a number')
#         # except IndexError:


        
# def validate_guess(guessers_board, opponents_board):
#     """
#     Validate the co-ordinates given that they are not a string.
#     Validate the guesses entered by the user playing, guesses need to be
#     within the boardsize and can't guess a co-ordinate that has already been guessed.
#     """
#     while True:
#         try:
#             num1 = int(input(f'Enter a number between 0 and {opponents_board.size - 1} for the X co-ordinate: \n'))
#             print(f'X co-ordinate selected is {num1}')
#             num2 = int(input(f'Enter a number between 0 and {opponents_board.size - 1} for the Y co-ordinate: \n'))
#             print(f'Y co-ordinate selected is {num2}')
#             (num1, num2) in guessers_board.player.guesses
#             print("please select a co-ordinate that hasn't already been chosen")
#             return opponents_board.guess(num1, num2)

#         except ValueError as error:
#             e = str(error).split()
#             print(f'{e[-1]} is not a number')
#         except IndexError:
#             print(f" Index values provided are out of range, please select a number between 0 and {opponents_board.size - 1}")
        # except Exception as already_targeted:
        #     print("please select a co-ordinate that hasn't already been chosen")

        # guessers_board.player.guesses
        # finally:
        #     return opponents_board.guess(num1, num2)


# def make_guess(guessers_board, opponents_board):
#     """
#     prompt the user to make a guess that is stored in the player.guesses list
#     """
#     if guessers_board.player.player_type == "user":
#         print("please enter the coordinates you would like to strike")
#         # validate_guess(guessers_board, opponents_board)
#     else:
#         while True:          # While false: check if (x, y) in guessers_board
#             try:
#                 x = int(random_int(guessers_board.size - 1))
#                 y = int(random_int(guessers_board.size - 1))
#                 coordinate = (x, y)
#                 print(x, y)
#                 coordinate not in guessers_board.player.guesses
#             #     opponents_board.guess(coordinate) #*
#             finally: 
#                 return opponents_board.guess(x, y)
#     return


#--------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------
# print()
# print(f"{player1.player_name}'s Battleship Board")
# print("-" * 40)
# print()
# players_board.display_board()
# print(f"{player2.player_name}'s Battleship Board")
# print("-" * 40)
# computers_board.display_board()
# print()
#----------------------------------------------------------------------------

# print(players_board.player.ships)
# print(computers_board.player.ships)
# print()
# print((1, 0) in players_board.player.ships)
# print((2, 0) in players_board.player.ships)
# print((3, 0) in players_board.player.ships)
# print()

#----------------------------------------------------------------------------

# code_checker_variable = make_guess(players_board, computers_board) 
# code_checker_variable = make_guess(computers_board, players_board) 
# print(code_checker_variable in computers_board.player.ships)

#----------------------------------------------------------------------------

# print()
# print(f"{player1.player_name}'s Battleship Board")
# print("-" * 40)
# print()
# players_board.display_board()
# print(f"{player2.player_name}'s Battleship Board")
# print("-" * 40)
# computers_board.display_board()
# print()
