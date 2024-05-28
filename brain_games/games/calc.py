import random


def calc_logic():
    random_num1 = random.randint(1, 30)
    random_num2 = random.randint(1, 30)
    operations = ["+", "-", "*"]
    random_element = random.choice(operations)
    question = f"Question: {random_num1} {random_element} {random_num2}"
    answer = str(eval(f'{random_num1} {random_element} {random_num2}'))
    return question, answer


def exercise():
    exercise = 'What is the result of the expression?'
    return exercise
