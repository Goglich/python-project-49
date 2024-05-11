from brain_games.engine import game
from brain_games.games.prime import prime_logic
from brain_games.games.prime import start_question


def main():
    game(prime_logic, start_question)

if __name__ == '__main__':
    main()