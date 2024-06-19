import random


DESCRIPTION = 'What number is missing in the progression?'
MIN_STEP, MAX_STEP = 2, 9
MIN_NUMBERS_QUANTITY, MAX_NUMBERS_QUANTITY = 5, 10
MIN_FIRST_NUM, MAX_FIRST_NUM = 1, 5
MIN_REPLACE_NUM = 1


def generate_game():
    step = random.randint(MIN_STEP, MAX_STEP)
    quantity = random.randint(MIN_NUMBERS_QUANTITY, MAX_NUMBERS_QUANTITY)
    first_num = random.randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    missing_num = random.randint(MIN_REPLACE_NUM, quantity)
    progression = [first_num]
    current_progression_len = 1

    for nums in range(1, quantity):
        progression.append(first_num + step * current_progression_len)
        current_progression_len += 1

    missing_index = missing_num - 1
    progression[missing_index] = '..'
    answer = str(first_num + missing_index * step)
    str_progression = [str(n) for n in progression]
    question = ' '.join(str_progression)

    return question, answer
