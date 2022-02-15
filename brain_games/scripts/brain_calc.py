#!/usr/bin/env python
"""Calculation game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.calc_game import run_calc_game, set_task_calc_game


def main():
    """Run calculation game."""
    run_game_logic(set_task_calc_game, run_calc_game)


if __name__ == '__main__':
    main()
