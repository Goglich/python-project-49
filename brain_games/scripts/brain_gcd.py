from brain_games.engine import game
from brain_games.games.gcd import gcd_logic
from brain_games.games.gcd import start_question

def main():
    game(gcd_logic, start_question)

if __name__ == 'main':
    main()