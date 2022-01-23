"""greeting module."""
import prompt


def welcome_user():
    """
    Greet user, get user name, return user name - return str.

    Returns:
        str: user name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name, sep=' ', end='!\n')
    return name
