from brain_games.engine import game
from brain_games.games.progression import progression_logic
from brain_games.games.progression import start_question


def main():
    game(progression_logic, start_question)

if __name__ == '__main__':
    main()