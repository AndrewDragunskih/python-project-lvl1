"""Prime game logic ."""
from random import randint


def is_number_prime(number):
    """
    Check if the number is prime.

    Args:
        number (int) : the number

    Returns:
        bool: True if the number is prime, else - false
    """
    current_num = 2
    answer = True
    if number == 1:
        answer = False
    while current_num <= number // 2 and answer is True:
        if number % current_num == 0:
            answer = False
        current_num += 1
    return answer


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
    # generate question to user
    question = randint(num_min, num_max)
    # generate right answer
    if is_number_prime(question) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer


def set_task_prime_game():
    """Print the task in prime game."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
