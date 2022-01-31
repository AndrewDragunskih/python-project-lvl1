#!/usr/bin/env python
"""Even game."""
from brain_games.games.gcd_game import run_gcd_game
from brain_games.greeting_user import welcome_user
from brain_games.results_processing import check_result
from brain_games.setting_the_task import set_the_task_gcd_game


def main():
    """Check the number os even or odd."""
    # Greeting user. Getting user name
    usr_name = welcome_user()
    # Setting the task
    set_the_task_gcd_game()
    # Initialize game parameters
    attmp_count = 3
    current_attmp = 1
    answer = ''
    right_answer = ''
    # run game
    while (current_attmp <= attmp_count) and (answer == right_answer):
        # run calc game. Get user answer and right answer
        answer, right_answer = run_gcd_game()
        # check if user answer is right
        check_result(current_attmp, attmp_count, usr_name, answer, right_answer)
        current_attmp += 1


if __name__ == '__main__':
    main()
