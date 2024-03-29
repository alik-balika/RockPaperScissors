"""
This file defines constants for a simple rock-paper-scissors game.

The constants represent the player's choices of rock, paper, and scissors,
which are assigned str values for ease of use in the game's logic.

Constants:
    ROCK (str): Represents the player's choice of rock, assigned the character value R.
    PAPER (str): Represents the player's choice of paper, assigned the character value P.
    SCISSORS (str): Represents the player's choice of scissors, assigned the character value S.
"""

ROCK = "R"
PAPER = "P"
SCISSORS = "S"
COMPUTER_MOVES = [ROCK, PAPER, SCISSORS]
CHARACTER_TO_WORD = {"R": "Rock", "P": "Paper", "S": "Scissors"}
SCORE_TO_REACH = 3
QUIT = "Q"
NUM_OPTIONS = 2

ROCK_INDEX = 0
PAPER_INDEX = 1
SCISSORS_INDEX = 2

EVENT_FOR_WAITING_AFTER_CHOICE = 1

DARK_BLUE = (0, 0, 139)
DARK_ORANGE = (250, 40, 40)
LIGHT_ORANGE = (252, 96, 96)
RED = (255, 0, 0)
GAME_FONT = "baskervilleoldface"
TITLE_FONT_SIZE = 50
REGULAR_FONT_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 60

# screen enums
TITLE_SCREEN = "TITLE"
PLAY_SCREEN = "PLAY"
END_SCREEN = "END"

ROCK_LOGO_DIMENSIONS = (55, 150, 80, 165)
PAPER_LOGO_DIMENSIONS = (230, 340, 70, 170)
SCISSORS_LOGO_DIMENSIONS = (145, 275, 205, 300)
START_BUTTON_DIMENSIONS = (
    SCREEN_WIDTH / 2 - 100, SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2 + 190, SCREEN_HEIGHT / 2 + 250)
