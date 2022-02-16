"""Calculation game ."""
from random import choice, randint

RANGE_START = 1
RANGE_END = 15
OPS = ('+', '-', '*')


def run_calc_game():
    """
    Run calculation game.

    Returns:
        str: answer
        str: right_answer
    """
    # generate question
    num1 = randint(RANGE_START, RANGE_END)
    num2 = randint(RANGE_START, RANGE_END)
    operator = choice(OPS)
    question = '{0} {1} {2}'.format(str(num1), operator, str(num2))
    # calculate right answer
    if operator == '+':
        right_answer = num1 + num2
    elif operator == '-':
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return question, str(right_answer)


def get_task_calc_game():
    """
    Print the task in calc game.

    Returns:
        str : calc game task
    """
    return 'What is the result of the expression?'
