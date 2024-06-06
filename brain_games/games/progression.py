import random


EXERCISE = 'What number is missing in the progression?'


def generate_game():
    step = random.randint(2, 9)
    quantity = random.randint(5, 10)
    first_num = random.randint(1, 5)
    replace_num = random.randint(5, quantity)
    progression = str(first_num)
    current_quantity = 1
    while current_quantity <= quantity:
        if current_quantity == replace_num:
            answer = str(first_num + step * current_quantity)
            progression += ' ' + '..'
            current_quantity += 1
        else:
            progression += ' ' + str(first_num + step * current_quantity)
            current_quantity += 1
    question = progression
    return question, answer
