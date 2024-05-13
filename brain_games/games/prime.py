import random


def prime_logic():
    num = random.randint(2, 50)
    print(num)
    counter = 1
    divider = 1
    answer = ""
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
        answer = "no"
    else:
        answer = "yes"
    question = f'Question: {num}'
    return question, answer


def exercise():
    exercise = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return exercise
