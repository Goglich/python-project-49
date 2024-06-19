import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 50


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def generate_game():
    random_num = random.randint(MIN_NUM, MAX_NUM)
    question = random_num

    if is_even(random_num):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
