import random


def even_logic():
    random_num = random.randint(1, 50)
    question = f"Question: {random_num}"

    if random_num % 2 == 0:
        answer = 'yes'
    elif random_num % 2 != 0:
        answer = 'no'
    return question, answer


def exercise():
    exercise = 'Answer "yes" if the number is even, otherwise answer "no".'
    return exercise
