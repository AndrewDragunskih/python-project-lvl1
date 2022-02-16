"""Greatest common divisor game ."""
from math import gcd
from random import randint

RANGE_START = 1
RANGE_END = 30


def run_gcd_game():
    """
    Run gcd game.

    Returns:
        str: answer
        str: right_answer
    """
    # generate random numbers
    num1 = randint(RANGE_START, RANGE_END)
    num2 = randint(RANGE_START, RANGE_END)
    # generate quesion to user
    question = '{0} {1}'.format(num1, num2)
    return question, str(gcd(num1, num2))


def get_task_gcd_game():
    """Print the task in gcd game.

    Returns:
        str : gcd game task
    """
    return 'Find the greatest common divisor of given numbers.'
