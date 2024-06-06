import random


EXERCISE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 2
MAX_NUM = 50


def is_prime(num):
    counter = 1  # counter will show how many times
    # the number has been divided without a remainder
    divider = 1
    while counter < 3:
        while divider <= num:
            if num % divider == 0:
                divider += 1
                counter += 1
                continue
            else:
                divider += 1
                continue
    if counter > 3:
        return False
    else:
        return True


def generate_game():
    num = random.randint(MIN_NUM, MAX_NUM)
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    question = num
    return question, answer
