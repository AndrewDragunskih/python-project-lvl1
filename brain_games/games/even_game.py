#!/usr/bin/env python
"""Even game logic ."""
from random import randint

RANGE_START = 1
RANGE_END = 50
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_q_and_a_even_game():
    """
    Check the number os even or odd.

    Returns:
        str: answer
        str: right_answer
    """
    question = randint(RANGE_START, RANGE_END)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
