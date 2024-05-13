from brain_games.engine import game
from brain_games.games.prime import prime_logic
from brain_games.games.prime import exercise


def main():
    game(prime_logic, exercise)


if __name__ == '__main__':
    main()
