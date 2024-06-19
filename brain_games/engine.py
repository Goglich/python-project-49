from brain_games.cli import welcome_user
import prompt


ROUNDS_COUNT = 3


def play_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_COUNT):
        question, answer = game.generate_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
