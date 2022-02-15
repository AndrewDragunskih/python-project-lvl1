"""Greatest common divisor game ."""
from math import gcd
from random import randint


def run_gcd_game():
    """
    Run gcd game.

    Returns:
        str: answer
        str: right_answer
    """
    # Ititialization
    range_start = 1
    range_end = 30
    # generate random numbers
    num1 = randint(range_start, range_end)
    num2 = randint(range_start, range_end)
    # generate quesion to user
    question = '{0} {1}'.format(num1, num2)
    return question, str(gcd(num1, num2))


def set_task_gcd_game():
    """Print the task in gcd game."""
    print('Find the greatest common divisor of given numbers.')
