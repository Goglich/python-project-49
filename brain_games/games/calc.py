import random


def calc_logic():
    random_num1 = random.randint(1,10)
    random_num2 = random.randint(1,10)
    operations = ["+" , "-", "*"]
    random_element = random.choice(operations)
    question = f"Question:  {random_num1} {random_element} {random_num2}"
    right_answer  = str(eval(f'{random_num1} {random_element} {random_num2}'))
    return question, right_answer


def start_question():
    start_quest = 'What is the result of the expression?'
    return start_quest