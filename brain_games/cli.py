"""greeting module."""

import prompt


def welcome_user():
    """Greeting new user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
