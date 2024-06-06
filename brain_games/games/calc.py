import random


EXERCISE = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 30


def generate_game():
    random_num1 = random.randint(MIN_NUM, MAX_NUM)
    random_num2 = random.randint(MIN_NUM, MAX_NUM)
    operations = ['+', '-', '*']
    random_element = random.choice(operations)
    question = f'{random_num1} {random_element} {random_num2}'
    answer = str(eval(f'{random_num1} {random_element} {random_num2}'))
    return question, answer
