import random

scores = {"computer": 0}


class AlreadyGuessedError(Exception):
    """
    This error is raised when the guesses list is being check against the
    new given guess coordinates.
    """


class OutOfRangeError(Exception):
    """
    This error is raised when the co-ordinate guessed is out of range
    of the size of the board.
    """


class TooSmallValueError(Exception):
    """
    This error is raised when the co-ordinate guessed is less than 0.
    """


class WhiteSpaceError(Exception):
    """
    This error is raised when the input consists any whitespace in the name.
    """


class NoNameEnteredError(Exception):
    """
    This error is raised when the input doesn't have any value inside the name.
    """


class GameBoard():
    """
    This is the model for the game board class. Here inside the Game_Board
    Class you can set the size of the board, the number of ships, the board
    player (computer or user)
    """
    def __init__(self, size, num_of_ships, player_type, player_name, turns):
        self.size = size
        self.board_grid = [["." for x in range(size)] for y in range(size)]
        self.num_of_ships = num_of_ships
        self.player_type = player_type
        self.player_name = player_name
        self.guesses = []
        self.ships = []
        self.turns = turns

    def display_board(self):
        for row in self.board_grid:
            print("  ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board_grid[x][y] = "X"
        self.turns += 1

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
    Helper function that creates a random interger based on the boardsize
    """
    return int(random.randint(0, boardsize - 1))


def add_ships_to_board(gameboard):
    """
    This function generates the random location of ships to the board.
    It takes the players_board and computers_board as the arguments
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


def input_coordinate(boardsize, row_or_column):
    """
    input a coordinate
    """
    text_a = ("Enter a number between 0 and ")
    num = int(input(text_a + f'{boardsize - 1} for the {row_or_column}: \n'))
    return num


def make_guess(gameboard, x, y):
    """
    Prompt the user to make a guess that is stored in the
    player.guesses list and returns the co-ordinates
    """
    return gameboard.guess(x, y)


def validate_input(gameboard, row_or_column):
    """
    Validate the input co-ordinate given to make sure that the input
    provided is valid to the dimensions of the board and that it is an
    interger
    """
    while True:
        try:
            num = input_coordinate(gameboard.size, row_or_column)
            if num > gameboard.size - 1:
                raise OutOfRangeError
            elif num < 0:
                raise TooSmallValueError
            return num
        except ValueError as error:
            e = str(error).split()
            print(f'{e[-1]} is not a valid input')
        except OutOfRangeError:
            print("The number provided is out of range")
        except TooSmallValueError:
            print("The number chosen has to be greater than 0")


def validate_name_input():
    """
    Validates the name of the player to make sure there is no whitespace
    """
    while True:
        try:
            name = str(input("What is your name? \n"))
            if " " in name:
                raise WhiteSpaceError
            if len(name) == 0:
                raise NoNameEnteredError
            return name
        except WhiteSpaceError:
            print("Please enter a name with no spaces")
        except NoNameEnteredError:
            text_a = ("You have to enter some form of name, be it a number")
            text_b = (", special character or one letter to play this game")
            print(text_a + text_b)


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
                    raise AlreadyGuessedError
            else:
                x = int(random_number(gameboard.size))
                y = int(random_number(gameboard.size))
                if (x, y) in gameboard.guesses:
                    raise AlreadyGuessedError
            return make_guess(gameboard, x, y), x, y
        except AlreadyGuessedError:
            if gameboard.player_type == "computer":
                text_a = ("please select a co-ordinate that ")
                text_b = ("hasn't already been chosen")
                print(text_a + text_b)


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


def shots_fired_counter(gameboard):
    """
    calculates the ammount of turns it takes for the player to win
    the game.
    """
    turns = gameboard.turns
    print()
    print("-" * 40)
    print("All targets were located, and destroyed. Well played soldier!")
    print(f"You fired {turns} shots to abliterate the enemy boats.")
    print()
    if int(turns) < 5:
        print("WOW!")
        print("Amazing accuracy, you have a keen aim and waste no shells!")
        print("You should get a medal of honor for your heroics!")
    elif int(turns) < 10:
        print("That is an impressive display. Your shots hit true!")
        print("Keep up that great work soldier!")
    elif int(turns) < 15:
        print("Good work and well fought, that was a tough battle!")
        print("You came out on top and showed them who is boss!")
    elif int(turns) < 20:
        print("Well done, you downed your opponent in less than 20 shots")
        print("That is a respectable score! Good work!")
    else:
        print("That was a really slog of a battle!")
        print("That was done to the wire, well done for coming out on top!")
    print("-" * 40)


def board_display(players_board, computers_board):
    """
    board display function is a helper function that consolidates a
    repeatable piece of code that is used in the game.
    """
    print()
    print(f"{players_board.player_name}'s Battleship Board")
    print("-" * 40)
    players_board.display_board()
    print()
    print(f"{computers_board.player_name}'s Battleship Board")
    print("-" * 40)
    computers_board.display_board()
    print()


def playgame(players_board, computers_board):
    """
    This function takes the player and the computer players as parameters
    and calls the functions to make guesses in the game until there is
    a winner. The function is carries a lot of the weight of the program.
    core concept to remember is that the guesses of a player are stored in
    the other gameboard guesses.
    """
    while scores["computer"] or scores[players_board.player_name] <= 4:
        print(f"{players_board.player_name}. It is your turn to attack!")
        print("Prepare to enter the co-ordinates you would like to strike.")
        print("-" * 65)
        players_turn, x, y = validate_input_coordinates(computers_board)

        print("-" * 65)
        print(f"Shot fired!, target '{players_turn}' at co-ordinate{(x, y)}")
        calculate_score(players_turn, players_board)
        if (scores[players_board.player_name] == 4):
            print()
            break

        print("-" * 65)
        print(f"It's now the {computers_board.player_name}'s turn to attack.")
        computers_turn, x, y = validate_input_coordinates(players_board)
        print("-" * 65)
        calculate_score(computers_turn, computers_board)
        print(f"Shot fired!, target '{computers_turn}' at co-ordinate{(x, y)}")
        if (scores["computer"] == 4):
            print()
            break

        board_display(players_board, computers_board)
        print("The scores at the end of the round are:")
        print(scores)
        print()

    board_display(players_board, computers_board)
    if scores[players_board.player_name] == 4:
        print(f"Congratulations {players_board.player_name}! You won!")
        shots_fired_counter(computers_board)
    else:
        print("Unlucky, The computer beat you this time!")
    print()
    print("The scores at the end of the game are:")
    print(scores)
    print()

    text_a = ("Would you like to play again? ")
    text_b = ("Press any key to continue or 'n' to quit:")
    play_again = str(input(text_a + text_b + " \n"))
    if play_again != "n":
        scores.pop(players_board.player_name)
        start_game()


def start_game():
    """
    runs the game and instatiates all the variables required to run the game
    """

    boardsize = 5
    ships = 4
    players_name = validate_name_input()
    scores["computer"] = 0
    scores[players_name] = 0
    turns = 0
    players_board = GameBoard(boardsize, ships, "user", players_name, turns)
    comptr_board = GameBoard(boardsize, ships, "computer", "Computer", turns)

    print()
    print("*" * 40)
    print("Welcome to the BattleShips Board!")
    print(f"The Board size: {boardsize}, The number of ships: {ships}")
    print("The top left grid co-ordinate is (0, 0)")
    print("*" * 40)

    add_ships_to_board(players_board)
    add_ships_to_board(comptr_board)

    board_display(players_board, comptr_board)
    playgame(players_board, comptr_board)


print()
print("-" * 65)
print("Welcome to BATTLESHIPS! This is turn-based stratergy game were")
print("the players take turns guessing co-ordinates on a grid to")
print("shoot and take out your opponents ships before they take out")
print("yours. The first one to take out all of each others ships wins!")
print("-" * 65)
print()
start_game()
