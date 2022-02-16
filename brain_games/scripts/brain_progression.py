#!/usr/bin/env python
"""Progression game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.progression_game import (
    get_task_progression_game,
    run_progression_game,
)


def main():
    """Find missing number in the progression."""
    run_game_logic(get_task_progression_game, run_progression_game)


if __name__ == '__main__':
    main()
