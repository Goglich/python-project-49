from brain_games.cli import welcome_user
import prompt


def game(logic, start_question):
    name = welcome_user()
    correct = 0
    start_quest = start_question()
    print(start_quest)
    while correct < 3:
        question, right_answer = logic()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            correct +=1
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {right_answer}. Let's try again, {name}")
            correct = 0
            return correct
        
    if correct == 3:
        print(f'Congratulations, {name}!')