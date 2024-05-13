from brain_games.engine import game
from brain_games.games.gcd import gcd_logic
from brain_games.games.gcd import exercise


def main():
    game(gcd_logic, exercise)


if __name__ == 'main':
    main()
