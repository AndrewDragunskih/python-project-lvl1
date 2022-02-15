#!/usr/bin/env python
"""Even game logic ."""
from random import randint


def run_even_game():
    """
    Check the number os even or odd.

    Returns:
        str: answer
        str: right_answer
    """
    # Initialization
    range_start = 1
    range_end = 100
    # generate question to user
    question = randint(range_start, range_end)
    # generate right answer
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def set_task_even_game():
    """Print the task in even game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
