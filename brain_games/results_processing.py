"""Processing results module ."""


def check_result(current_attmp, attmp_count, user_name, answer, right_answer):
    """
    Say result to user.

    Args:
        current_attmp (int): number of current game
        attmp_count (int): count of games
        user_name (str): name of the user
        answer (str): user answer
        right_answer (str): calculated answer
    """
    if answer == right_answer and current_attmp < attmp_count:
        print('Correct!')
    elif answer == right_answer and current_attmp == attmp_count:
        print('Correct!')
        print('Congratulations,', user_name, sep=' ', end='!\n')
    else:
        print("'{0}' is wrong answer ;(.".format(answer), end=' ')
        print("Correct answer was '{0}'.".format(right_answer))
        print("Let's try again, {0}!".format(user_name))
