"""Progression game logic."""
from random import randint


def run_progression_game():
    """
    Run progression game.

    Returns:
        str: answer
        str: right_answer
    """
    # initialization
    prog_len_max = 10
    prog_len_min = 5
    prog_len = randint(prog_len_min, prog_len_max)
    num_max = 25
    num_min = 1
    init_num = randint(num_min, num_max)
    diff = randint(num_min, num_max)
    pos_to_find = randint(1, prog_len)
    question = ''
    # generate progression and choose number to find
    for num_pos in range(1, prog_len + 1):
        if num_pos == pos_to_find:
            question = '{0}..'.format(question)
            right_answer = str(init_num + (num_pos - 1) * diff)
        else:
            question += str(init_num + (num_pos - 1) * diff)
        if num_pos < prog_len:
            question = '{0} '.format(question)
    # ask user a question
    print('Question:', question)
    # get user answer
    answer = input('Your answer: ')
    return answer, right_answer
