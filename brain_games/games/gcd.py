import math
import random


def gcd_logic():
    num1 = random.randint(2, 150)
    num2 = random.randint(2, 150)

    while math.gcd(num1, num2) == 1:
        num1 = random.randint(2, 150)
        num2 = random.randint(2, 150)
    answer = str(math.gcd(num1, num2))
    question = f"Question: {num1} {num2}"

    return question, answer


def exercise():
    exercise = 'Find the greatest common divisor of given numbers.'
    return exercise
