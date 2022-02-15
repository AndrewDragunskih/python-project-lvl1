#!/usr/bin/env python
"""Even game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.gcd_game import run_gcd_game, set_task_gcd_game


def main():
    """Check the number os even or odd."""
    run_game_logic(set_task_gcd_game, run_gcd_game)


if __name__ == '__main__':
    main()
