"""Progression game ."""
from random import randint

PROG_LEN_MIN = 10
PROG_LEN_MAX = 10
NUM_MIN = 1
NUM_MAX = 25
TASK = 'What number is missing in the progression?'


def generate_a_and_a_progression_game():
    """
    Run progression game.

    Returns:
        str: answer
        str: right_answer
    """
    prog_len = randint(PROG_LEN_MIN, PROG_LEN_MAX)
    init_num = randint(NUM_MIN, NUM_MAX)
    diff = randint(NUM_MIN, NUM_MAX)
    pos_to_find = randint(1, prog_len)
    question = ''
    for num_pos in range(1, prog_len + 1):
        if num_pos == pos_to_find:
            question = '{0}..'.format(question)
            right_answer = str(init_num + (num_pos - 1) * diff)
        else:
            question += str(init_num + (num_pos - 1) * diff)
        if num_pos < prog_len:
            question = '{0} '.format(question)
    return question, right_answer
