"""Setting the task module ."""


def set_the_task(game_name):
    """
    Set the task in running game.

    Args:
        game_name (str) : Name of running game
    """
    functions = {
        'calc': 'What is the result of the expression?',
        'even': 'Answer "yes" if the number is even, otherwise answer "no".',
        'gcd': 'Find the greatest common divisor of given numbers.',
        'prime': 'What number is missing in the progression?',
        'prg': 'Answer "yes" if given number is prime. Otherwise answer "no".',
    }
    print(functions[game_name])
