#!/usr/bin/env python
"""Progression game game."""
from brain_games.games.progression_game import run_progression_game
from brain_games.greeting_user import welcome_user
from brain_games.results_processing import check_result
from brain_games.setting_the_task import set_the_task_progression_game


def main():
    """Find missing number in the progression."""
    # Greeting user. Getting user name
    usr_name = welcome_user()
    # Setting the task
    set_the_task_progression_game()
    # Initialize game parameters
    attmp_count = 3
    current_attmp = 1
    answer = ''
    right_answer = ''
    # run game
    while (current_attmp <= attmp_count) and (answer == right_answer):
        # run game. Get user answer and right answer
        answer, right_answer = run_progression_game()
        # check if user answer is right
        check_result(current_attmp, attmp_count, usr_name, answer, right_answer)
        current_attmp += 1


if __name__ == '__main__':
    main()
