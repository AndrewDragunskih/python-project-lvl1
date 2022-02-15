"""Run logic in any game."""
import prompt


def run_game_logic(set_task_chosen_game, run_chosen_game):
    """
    Run game logic.

    Args:
        set_task_chosen_game : task to chosen game
        run_chosen_game : run chosen game
    """
    # Greeting user. Getting user name
    print('Welcome to the Brain Games!')
    usr_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(usr_name))
    set_task_chosen_game()
    # Initialize game parameters
    attmp_count = 3
    current_attmp = 1
    answer = ''
    right_answer = ''
    # run game
    while (current_attmp <= attmp_count) and (answer == right_answer):
        # run game. generate question to user and right answer
        question, right_answer = run_chosen_game()
        # print question to user and get user answer
        print('Question:', question)
        answer = input('Your answer: ')
        # check if user answer is right
        if answer == right_answer and current_attmp < attmp_count:
            print('Correct!')
        elif answer == right_answer and current_attmp == attmp_count:
            print('Correct!')
            print('Congratulations,', usr_name, sep=' ', end='!\n')
        else:
            print("'{0}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was '{0}'.".format(right_answer))
            print("Let's try again, {0}!".format(usr_name))
        current_attmp += 1
