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
    range_start = 1
    range_end = 100
    # generate random number
    question = randint(range_start, range_end)
    # ask user a question
    print('Question:', question)
    # get user answer
    answer = input('Your answer: ')
    # generate right answer
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return answer, right_answer
