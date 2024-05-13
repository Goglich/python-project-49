from brain_games.engine import game
from brain_games.games.even import even_logic
from brain_games.games.even import exercise


def main():
    game(even_logic, exercise)


if __name__ == 'main':
    main()
