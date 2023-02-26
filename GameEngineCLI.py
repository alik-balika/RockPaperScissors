from constants import *

player_score, computer_score = 0, 0


def start_game():
    player_input = input("Welcome to Rock Paper Scissors! Enter Q at any time to quit. \n"
                         "The goal of the game is to be the first player to get to 3.\n"
                         "To begin please enter any key: ")

    while player_input != "":
        player_input = input("\nPlease enter Rock(R), Paper(P), or Scissors(S): ")

        if player_input.upper() == QUIT:
            print(f"\nThanks for playing my game!\nFinal Score:\n\tPlayer: {player_score}\n\tComputer: {computer_score}")
            quit()
