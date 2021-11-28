# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random


class Player():
    """
    Player Class. creates a player object which holds the player type,
    name and their game board.
    """
    def __init__(self, player_name, player_type):
        self.player_name = player_name
        self.player_type = player_type
        self.guesses = []
        self.ships = []


class GameBoard():
    """
    This is the model for the game board class. Here inside the Game_Board
    Class you can set the size of the board, the number of ships, the board
    player (computer or user)
    """
    def __init__(self, size, num_of_ships, player):
        self.size = size
        self.board_grid = [["." for x in range(size)] for y in range(size)]
        self.num_of_ships = num_of_ships
        self.player = player

    def display_board(self):
        for row in self.board_grid:
            print("  ".join(row))

    def guess(self, x, y):
        self.player.guesses.append((x, y))
        self.board_grid[x][y] = "X"

        if (x, y) in self.player.ships:
            self.board_grid[x][y] = "@"
            return "Hit"
        else:
            return "Miss"

    def display_ships(self):
        # if len(self.player.ships) > self.num_of_ships:
        #     print("Error: you cannot add anymore ships to the board")
        # else:
        for co_ord in self.player.ships:
            x, y = co_ord
            if self.player.player_type == "user":
                self.board_grid[x][y] = "$"


def random_int(board_size):
    """
    a helper function that generates a random interger thats value
     ranges from 0 to the size of the board given.
    """
    return random.randint(0, board_size - 1)


players_name = input("What is your name? \n")

player1 = Player(players_name, "user")
player2 = Player("Computer", "computer")

players_board = GameBoard(5, 4, player1)
computers_board = GameBoard(5, 4, player2)


def add_ships_to_board(users_board):
    """
    This function generates the random location of ships to the board. it takes the
    players_board and computers_board as the arguments
    """
    num_of_ships = users_board.num_of_ships
    ship_list = []
    unique_coordinates = []

    while len(unique_coordinates) < num_of_ships:
        x = random_int(users_board.size)
        y = random_int(users_board.size)
        ship = (x, y)
        # print(ship) # program checker print
        ship_list.append(ship)
        unique_coordinates = set(ship_list)
        users_board.player.ships = list(unique_coordinates)
        users_board.display_ships()

    print(ship_list)
    print(unique_coordinates)


def make_guess(guessers_board, opponents_board):
    """
    prompt the user to make a guess that is stored in the player.guesses list
    """
    if guessers_board.player.player_type == "user":
        print("please enter the coordinates you would like to strike")
        x = input(f"please enter an x co-ordinate of 0 or no greater than {guessers_board.size - 1 }\n")
        y = input(f"please enter an y co-ordinate of 0 or no greater than {guessers_board.size - 1}\n")
        opponents_board.guess(int(x), int(y))
    else:
        x = random_int(guessers_board.size -1)
        y = random_int(guessers_board.size -1)
        opponents_board.guess(int(x), int(y))

# def validate_guess():


add_ships_to_board(players_board)
add_ships_to_board(computers_board)

#----------------------------------------------------------------------------
print()
print(f"{player1.player_name}'s Battleship Board")
print("-" * 40)
print()
players_board.display_board()
print(f"{player2.player_name}'s Battleship Board")
print("-" * 40)
computers_board.display_board()
print()
#----------------------------------------------------------------------------

print(players_board.player.ships)
print(computers_board.player.ships)
print()
print((1, 0) in players_board.player.ships)
print((2, 0) in players_board.player.ships)
print((3, 0) in players_board.player.ships)
print()

#----------------------------------------------------------------------------
code_checker_variable = make_guess(players_board, computers_board) 
code_checker_variable = make_guess(computers_board, players_board) 
print(code_checker_variable in computers_board.player.ships)
#----------------------------------------------------------------------------

print()
print(f"{player1.player_name}'s Battleship Board")
print("-" * 40)
print()
players_board.display_board()
print(f"{player2.player_name}'s Battleship Board")
print("-" * 40)
computers_board.display_board()
print()
