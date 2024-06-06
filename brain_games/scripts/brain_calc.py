from brain_games.engine import game
from brain_games.games.calc import generate_game
from brain_games.games.calc import EXERCISE


def main():
    game(generate_game, EXERCISE)


if __name__ == '__main__':
    main()
