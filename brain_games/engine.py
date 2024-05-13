from brain_games.cli import welcome_user
import prompt


def game(logic, exercise):
    name = welcome_user()
    correct = 0
    start_quest = exercise()
    print(start_quest)
    while correct < 3:
        question, answer = logic()
        print(question)
        us_ans = prompt.string('Your answer: ')
        if us_ans == answer:
            print('Correct!')
            correct += 1
        else:
            print(f"{us_ans} is wrong answer ;(. Correct answer was {answer}.")
            print(f"Let's try again, {name}")
            correct = 0
            return correct
    if correct == 3:
        print(f'Congratulations, {name}!')
