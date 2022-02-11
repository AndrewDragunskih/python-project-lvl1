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
    # Print game rules
    print('Find the greatest common divisor of given numbers.')
    # Ititialization
    range_start = 1
    range_end = 30
    # generate random numbers and operator
    num1 = randint(range_start, range_end)
    num2 = randint(range_start, range_end)
    # ask user a question
    print('Question: {0} {1}'.format(num1, num2))
    # get user answer
    answer = input('Your answer: ')
    return answer, str(gcd(num1, num2))
