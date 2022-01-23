#!/usr/bin/env python
"""Even game."""
from random import randint

from brain_games.greeting_user import welcome_user


def main():
    """Check the number os even or odd."""
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    range_start = 1
    range_end = 100
    attempts_count = 3
    current_attempt = 1
    is_user_answer_right = 1
    while (current_attempt <= attempts_count) and (is_user_answer_right == 1):
        question = randint(range_start, range_end)  # generate random number
        if question % 2 == 0:  # generate right answer
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question:', question)  # ask user a question
        print('Your answer:')  # get user answer
        answer = input()
        if answer == right_answer:  # check user answer
            print('Correct!')
            current_attempt += 1
        else:
            is_user_answer_right = 0
            print(answer, 'is wrong answer ;(.', end=' ')
            print('Correct answer was', right_answer, sep=' ')
            print("Let's try again,", user_name, end='!\n')
    if is_user_answer_right == 1:
        print('Congratulations,', user_name, sep=' ', end='!\n')


if __name__ == '__main__':
    main()
