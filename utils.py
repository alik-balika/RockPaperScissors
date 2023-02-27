import random

from constants import *


def calculate_computer_move() -> str:
    """
    Returns a randomly selected move from the list of possible moves for the computer.

    :return: A string representing the computer's move ("R", "P", or "S").
    """
    return random.choice(COMPUTER_MOVES)


def calculate_winner_of_round(player_move: str, computer_move: str) -> str:
    """
    This function determines the winner of the current round and returns who won.

    :param player_move: A string representing the player's move.
    :param computer_move: A string representing the computer's move.
    """
    winning_moves = {
        ROCK: SCISSORS,
        PAPER: ROCK,
        SCISSORS: PAPER
    }

    if winning_moves.get(player_move) == computer_move:
        return "Player"
    elif winning_moves.get(computer_move) == player_move:
        return "Computer"

    return ""
