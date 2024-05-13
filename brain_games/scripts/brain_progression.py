from brain_games.engine import game
from brain_games.games.progression import progression_logic
from brain_games.games.progression import exercise


def main():
    game(progression_logic, exercise)


if __name__ == '__main__':
    main()
