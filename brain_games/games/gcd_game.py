"""Greatest common divisor game ."""
from math import gcd
from random import randint

RANGE_START = 1
RANGE_END = 30
TASK = 'Find the greatest common divisor of given numbers.'


def generate_q_and_a_gcd_game():
    """
    Run gcd game.

    Returns:
        str: answer
        str: right_answer
    """
    num1 = randint(RANGE_START, RANGE_END)
    num2 = randint(RANGE_START, RANGE_END)
    question = '{0} {1}'.format(num1, num2)
    return question, str(gcd(num1, num2))
