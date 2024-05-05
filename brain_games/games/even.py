import random

def even_logic():
    random_num = random.randint(1,50)
    question = f"Question: {random_num}"

    if random_num % 2 == 0:
        right_answer = 'yes'
    elif random_num % 2 != 0:
        right_answer = 'no'
    
    return question, right_answer


def start_question():
    start_quest = 'Answer "yes" if the number is even, otherwise answer "no".'
    return start_quest