from brain_games.scripts.engine import game
from brain_games.games.calc import calc_logic
from brain_games.games.calc import start_question


def main():
    game(calc_logic, start_question)


if __name__ == 'main':
    main()