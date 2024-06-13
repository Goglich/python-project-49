import random


DESCRIPTION = 'What number is missing in the progression?'
MIN_STEP, MAX_STEP = 2, 9
MIN_NUMBERS_QUANTITY, MAX_NUMBERS_QUANTITY = 5, 10
MIN_FIRST_NUM, MAX_FIRST_NUM = 1, 5
MIN_REPLACE_NUM = 5


def generate_game():
    step = random.randint(MIN_STEP, MAX_STEP)
    quantity = random.randint(MIN_NUMBERS_QUANTITY, MAX_NUMBERS_QUANTITY)
    first_num = random.randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    replace_num = random.randint(MIN_REPLACE_NUM, quantity)
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
