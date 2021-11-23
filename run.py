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

    def add_ship_to_grid(self, x, y):
        if len(self.player.ships) > self.num_of_ships:
            print("Error: you cannot add anymore ships to the board")
        else:
            self.player.ships.append((x, y))
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


def populate_ships_to_board(users_board):
    """
    This function generates the random location of ships to the board. it takes the
    players_board and computers_board as the arguments
    """
    num_of_ships = users_board.num_of_ships

    for ship in range(0, num_of_ships):
        ship = users_board.add_ship_to_grid(random_int(users_board.size), random_int(users_board.size))
        while ship not in users_board.player.ships:
            users_board.player.ships.append(ship)


# find why there is a none object appearing in the list of ships

populate_ships_to_board(players_board)
populate_ships_to_board(computers_board)


print()
print(f"{player1.player_name}'s Battleship Board")
print("-" * 40)
print()
players_board.display_board()
print(f"{player2.player_name}'s Battleship Board")
print("-" * 40)
computers_board.display_board()
print()

print(players_board.player.ships)
print(computers_board.player.ships)
