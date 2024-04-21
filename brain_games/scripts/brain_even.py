import random
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')


def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    def quest(): 
        result = 0   
        random_num = random.randint(1,50)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')

        if random_num % 2 == 0 and answer == 'yes':
            print('Correct!')
            result += 1
        elif random_num % 2 != 0 and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}")
        elif random_num % 2 != 0 and answer == 'no':
            print('Correct!')
            result += 1
        elif random_num % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}")
        return result
    counter = 0
    if quest() > 0:
        while counter < 2:
            counter += 1
            quest()
    if counter == 2:
        print(f'Congratulations, {name}!')
game()