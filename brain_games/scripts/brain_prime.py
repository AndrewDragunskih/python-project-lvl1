#!/usr/bin/env python
"""Prime game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.prime_game import run_prime_game


def main():
    """Check the number is prime or not."""
    # Greeting user. Getting user name
    run_game_logic(run_prime_game)


if __name__ == '__main__':
    main()
