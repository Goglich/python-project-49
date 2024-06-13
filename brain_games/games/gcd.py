import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 2
MAX_NUM = 150


def generate_game():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    answer = str(math.gcd(num1, num2))
    question = f'{num1} {num2}'
    return question, answer
