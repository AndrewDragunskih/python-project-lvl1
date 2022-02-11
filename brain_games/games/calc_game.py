"""Calculation game ."""
from random import choice, randint


def run_calc_game():
    """
    Run calculation game.

    Returns:
        str: answer
        str: right_answer
    """
    # Print game rules
    print('What is the result of the expression?')
    # Ititialization
    range_start = 1
    range_end = 10
    ops = ['+', '-', '*']
    # generate random numbers and operator
    num1 = randint(range_start, range_end)
    num2 = randint(range_start, range_end)
    operator = choice(ops)
    question = '{0} {1} {2}'.format(str(num1), operator, str(num2))
    # ask user a question
    print('Question:', question)
    # get user answer
    answer = input('Your answer: ')
    # calculate right answer
    if operator == '+':
        right_answer = num1 + num2
    elif operator == '-':
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2
    return answer, str(right_answer)
