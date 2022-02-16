#!/usr/bin/env python
"""Even game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.even_game import get_task_even_game, run_even_game


def main():
    """Check the number os even or odd."""
    run_game_logic(get_task_even_game, run_even_game)


if __name__ == '__main__':
    main()
