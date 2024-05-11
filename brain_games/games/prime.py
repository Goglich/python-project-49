import random

def prime_logic():
    num = random.randint(2, 30)
    print(num)
    counter = 1
    divider = 1
    right_answer = ""
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
        right_answer = "no"
    else:
        right_answer = "yes"
    question = f'Question: {num}'  
    return question, right_answer

def start_question():
    start_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return start_question