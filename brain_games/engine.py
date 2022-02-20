"""Run logic in any game."""
import prompt

ATTEMPTS_COUNT = 3


def run_game_logic(task_chosen_game, get_q_and_a_chosen_game):
    """
    Run game logic.

    Args:
        task_chosen_game : task to chosen game
        get_q_and_a_chosen_game : run chosen game
    """
    print('Welcome to the Brain Games!')
    usr_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(usr_name))
    print(task_chosen_game)
    current_attmp = 1
    answer = ''
    right_answer = ''
    while current_attmp <= ATTEMPTS_COUNT:
        question, right_answer = get_q_and_a_chosen_game()
        print('Question:', question)
        answer = input('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            if current_attmp == ATTEMPTS_COUNT:
                print('Congratulations,', usr_name, sep=' ', end='!\n')
                break
        else:
            print("'{0}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was '{0}'.".format(right_answer))
            print("Let's try again, {0}!".format(usr_name))
            break
        current_attmp += 1
