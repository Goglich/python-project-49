from brain_games.engine import game
from brain_games.games.even import even_logic
from brain_games.games.even import start_question


def main():
    game(even_logic, start_question)



if __name__ == 'main':
    main()