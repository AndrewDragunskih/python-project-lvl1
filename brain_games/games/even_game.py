#!/usr/bin/env python
"""Even game logic ."""
from random import randint

RANGE_START = 1
RANGE_END = 50


def run_even_game():
    """
    Check the number os even or odd.

    Returns:
        str: answer
        str: right_answer
    """
    # generate question to user
    question = randint(RANGE_START, RANGE_END)
    # generate right answer
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def get_task_even_game():
    """
    Print the task in even game.

    Returns:
        str : even game task
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'
