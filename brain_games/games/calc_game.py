"""Calculation game ."""
from random import choice, randint

RANGE_START = 1
RANGE_END = 15
OPS = ('+', '-', '*')
TASK = 'What is the result of the expression?'


def generate_q_and_a_calc_game():
    """
    Run calculation game.

    Returns:
        str: answer
        str: right_answer
    """
    num1 = randint(RANGE_START, RANGE_END)
    num2 = randint(RANGE_START, RANGE_END)
    operator = choice(OPS)
    question = '{0} {1} {2}'.format(str(num1), operator, str(num2))
    if operator == '+':
        return question, str(num1 + num2)
    if operator == '-':
        return question, str(num1 - num2)
    if operator == '*':
        return question, str(num1 * num2)
