import random
from art import logo



def random_num():
    number = random.randint(1,100)
    return number
print(random_num())

def compare(num,guess_num):
    if guess_num == num:
        pass_guess = True

        return print(f"You got it! the answer was {num}{pass_guess}")
    elif guess_num > num:
        pass_guess = False
        return print(f"too high{pass_guess}")
    else:
        pass_guess = False
        return print(f"too low{pass_guess}")

game_level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100'.\nChoose a difficulty. Type \'easy\' or \'hard\': ").lower()

hard_attempts = 5
easy_attempts = 10
pass_guess  = False
if game_level == 'hard':
    computer_num = random_num()
    while not pass_guess:
        guess_num = int(input(f"You have {hard_attempts} attempts remaining to guess the number.\nMake a guess: "))
        hard_attempts -= 1
        print(guess_num,computer_num,hard_attempts)
        compare(computer_num,guess_num)
        # hard_attempts -= 1
        #


