"""Prime game logic."""
from random import randint


def run_prime_game():
    """
    Run prime game.

    Returns:
        str: answer
        str: right_answer
    """
    # initialization
    num_max = 100
    num_min = 1
    question = randint(num_min, num_max)
    current_num = 2
    # checking number
    if question == 1:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    while current_num <= question // 2 and right_answer == 'yes':
        if question % current_num == 0:
            right_answer = 'no'
        current_num += 1
    # ask user a question
    print('Question:', question)
    # get user answer
    answer = input('Your answer: ')
    return answer, right_answer
