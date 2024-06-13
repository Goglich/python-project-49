import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 2
MAX_NUM = 50


def is_prime(num):
    divider = 2
    while divider < num - 1:
        if num % divider == 0:
            return False
        else:
            divider += 1
    return True


def generate_game():
    num = random.randint(MIN_NUM, MAX_NUM)
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    question = num
    return question, answer
