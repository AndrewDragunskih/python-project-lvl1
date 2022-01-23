"""greeting module."""

import prompt


def welcome_user():
    """Greeting new user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name, sep = ' ', end = '!\n')
    return name
