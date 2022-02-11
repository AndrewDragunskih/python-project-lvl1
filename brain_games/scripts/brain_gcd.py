#!/usr/bin/env python
"""Even game script ."""
from brain_games.engine import run_game_logic
from brain_games.games.gcd_game import run_gcd_game


def main():
    """Check the number os even or odd."""
    # Greeting user. Getting user name
    run_game_logic(run_gcd_game)


if __name__ == '__main__':
    main()
