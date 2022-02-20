#!/usr/bin/env python
"""Prime game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.prime_game import TASK, generate_q_and_a_prime_game


def main():
    """Check the number is prime or not."""
    run_game_logic(TASK, generate_q_and_a_prime_game)


if __name__ == '__main__':
    main()
