import math
import random


def gcd_logic():

    num1 = random.randint(2, 150)
    num2 = random.randint(2, 150)

    while math.gcd(num1, num2) == 1:
        num1 = random.randint(2, 150)
        num2 = random.randint(2, 150)
    
    right_answer = str(math.gcd(num1, num2))
    question = f"Question : {num1} {num2}"

    return question, right_answer

def start_question():
    start_quest = 'Find the greatest common divisor of given numbers.'
    return start_quest