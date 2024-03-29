#!/usr/bin/env python
"""Even game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.even_game import TASK, generate_q_and_a_even_game


def main():
    """Check the number os even or odd."""
    run_game_logic(TASK, generate_q_and_a_even_game)


if __name__ == '__main__':
    main()
