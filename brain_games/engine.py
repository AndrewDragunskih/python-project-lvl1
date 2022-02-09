"""Run logic in any game."""
from brain_games.games.calc_game import run_calc_game
from brain_games.games.even_game import run_even_game
from brain_games.games.gcd_game import run_gcd_game
from brain_games.games.prime_game import run_prime_game
from brain_games.games.progression_game import run_progression_game
from brain_games.greeting_user import welcome_user
from brain_games.results_processing import check_result
from brain_games.setting_the_task import set_the_task


def run_game_logic(game_name):
    """
    Run game logic.

    Args:
        game_name (str) : Name of running game
    """
    # Greeting user. Getting user name
    usr_name = welcome_user()
    # Setting the task
    set_the_task(game_name)
    # Initialize game parameters
    attmp_count = 3
    current_attmp = 1
    answer = ''
    right_answer = ''
    # run game
    functions = {
        'calc': run_calc_game,
        'even': run_even_game,
        'gcd': run_gcd_game,
        'prime': run_prime_game,
        'prg': run_progression_game,
    }
    while (current_attmp <= attmp_count) and (answer == right_answer):
        # run game. Get user answer and right answer
        answer, right_answer = functions[game_name]()
        # check if user answer is right
        check_result(current_attmp, attmp_count, usr_name, answer, right_answer)
        current_attmp += 1
