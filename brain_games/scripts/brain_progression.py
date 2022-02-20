#!/usr/bin/env python
"""Progression game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.progression_game import (
    TASK,
    generate_q_and_a_progression_game,
)


def main():
    """Find missing number in the progression."""
    run_game_logic(TASK, generate_q_and_a_progression_game)


if __name__ == '__main__':
    main()
