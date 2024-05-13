from brain_games.engine import game
from brain_games.games.calc import calc_logic
from brain_games.games.calc import exercise


def main():
    game(calc_logic, exercise)


if __name__ == 'main':
    main()
