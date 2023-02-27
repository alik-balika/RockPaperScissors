"""
This file tuns the rock paper scissors game in the CLI form.

The game is played in the console and the player is prompted with instructions.
It is a simple game of rock, paper, scissors with the basic rules.
"""

import time

from utils import *


def is_valid_input(player_input: str) -> bool:
    """
    This function checks if the player input is valid and is one of ("R, "P", "S", or "Q").

    :param player_input: A string containing the input from the player.
    :return: True if the input is valid or False otherwise.
    """
    return player_input in COMPUTER_MOVES or player_input == QUIT


class GameCLI:
    def __init__(self):
        """
        This function initializes a new instance of the GameCLI class with both
        the player's and computer's scores set to zero.
        """
        self.player_score = 0
        self.computer_score = 0

    def start_game(self):
        """
        This function starts the game and continues until either the player or
        computer reaches the SCORE_TO_REACH constant. The player is prompted to
        input a move, while the computer selects a random move. The function
        then calculates the winner of the round and updates the scores.
        """
        print(f"Welcome to Rock Paper Scissors! Enter {QUIT} at any time to quit.")
        print(f"The goal of the game is to be the first player to get to {SCORE_TO_REACH}.")
        input("Press Enter to begin.")

        while True:
            print("\nComputer is thinking...")
            time.sleep(1.5)
            computer_move = calculate_computer_move()
            print("Computer has chosen a move!\n")
            player_move = input(f"Please enter {ROCK}, {PAPER}, or {SCISSORS}: ").upper()

            while not is_valid_input(player_move):
                player_move = input(f"Please enter only {ROCK}, {PAPER}, {SCORE_TO_REACH}, or {QUIT}: ")

            if player_move == QUIT:
                self.print_final_scores()
                quit()

            print(f"Computer chose {CHARACTER_TO_WORD[computer_move]}!")
            print(f"You chose {CHARACTER_TO_WORD[player_move]}!")

            winner = calculate_winner_of_round(player_move, computer_move)

            if winner == "Player":
                print("Player won this round!")
                self.player_score += 1
            elif winner == "Computer":
                print("Computer won this round!")
                self.computer_score += 1

            print("\nScore:")
            self.print_scores()

            if self.player_score == SCORE_TO_REACH or self.computer_score == SCORE_TO_REACH:
                break

        self.print_final_scores()

    def print_scores(self):
        """
        This function prints the current scores of both the player and computer.
        """
        print(f"\tPlayer: {self.player_score}\n\tComputer: {self.computer_score}")

    def print_final_scores(self):
        """
        This function prints the final scores and a thank you message to the player.
        """
        print(
            f"\nThanks for playing the game!\nFinal Score:")
        self.print_scores()
