"""Prime game logic ."""
from random import randint

RANGE_START = 1
RANGE_END = 100
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number_prime(number):
    """
    Check if the number is prime.

    Args:
        number (int) : the number

    Returns:
        bool: True if the number is prime, else - false
    """
    current_num = 2
    if number == 1:
        return False
    while current_num <= number // 2:
        if number % current_num == 0:
            return False
        current_num += 1
    return True


def generate_q_and_a_prime_game():
    """
    Run prime game.

    Returns:
        str: answer
        str: right_answer
    """
    question = randint(RANGE_START, RANGE_END)
    if is_number_prime(question) is True:
        return question, 'yes'
    return question, 'no'
