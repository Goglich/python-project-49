from brain_games.engine import game
from brain_games.games.progression import generate_game
from brain_games.games.progression import EXERCISE


def main():
    game(generate_game, EXERCISE)


if __name__ == '__main__':
    main()
