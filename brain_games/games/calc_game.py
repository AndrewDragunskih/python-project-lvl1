"""Calculation game ."""
from random import choice, randint


def run_calc_game():
    """
    Run calculation game.

    Returns:
        str: answer
        str: right_answer
    """
    # Ititialization
    range_start = 1
    range_end = 10
    ops = ['+', '-', '*']
    # generate question
    num1 = randint(range_start, range_end)
    num2 = randint(range_start, range_end)
    operator = choice(ops)
    question = '{0} {1} {2}'.format(str(num1), operator, str(num2))
    # calculate right answer
    if operator == '+':
        right_answer = num1 + num2
    elif operator == '-':
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return question, str(right_answer)


def set_task_calc_game():
    """Print the task in calc game."""
    print('What is the result of the expression?')
