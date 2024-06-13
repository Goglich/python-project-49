from brain_games.cli import welcome_user
import prompt


ROUNDS_QUANTITY = 3


def engine_game(game):
    name = welcome_user()
    start_quest = game.DESCRIPTION
    print(start_quest)
    for _ in range(ROUNDS_QUANTITY):
        question, answer = game.generate_game()
        print(f'Question: {question}')
        us_ans = prompt.string('Your answer: ')
        if us_ans == answer:
            print('Correct!')
        else:
            print(f'{us_ans} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
