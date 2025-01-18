import random
from art import logo

#chose random number from 1-100
def random_num():
    '''Generate random number from 1-100'''
    number = random.randint(1,100)
    return number

#choose game level
def game_level():
    difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100'.\nChoose a difficulty. Type \'easy\' or \'hard\': ").lower()
    if difficulty == "easy":
        return  10
    elif difficulty == "hard":
        return  5

def compare(num, guess):
    '''Compare 2 inputs value'''
    if guess == num:
        return print(f"You got it! the answer was {num}")
    elif guess > num:
        return print(f"too high\nGuess again")
    else:
        return print(f"too low\nGuess again")

print(logo)
# game_level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100'.\nChoose a difficulty. Type \'easy\' or \'hard\': ").lower()
#
# hard_attempts = 5
# easy_attempts = 10
attempts = game_level()
game_over  = False
computer_num = random_num()
while not game_over:
    guess_num = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
    attempts -= 1
    print(guess_num,computer_num,attempts)
    compare(computer_num,guess_num)

    if guess_num == computer_num:
        game_over = True
    elif attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        game_over = True


# if game_level == 'hard':
#     while not game_over:
#         guess_num = int(input(f"You have {hard_attempts} attempts remaining to guess the number.\nMake a guess: "))
#         attempts -= 1
#         print(guess_num,computer_num,hard_attempts)
#         compare(computer_num,guess_num)
#
#         if guess_num == computer_num:
#             game_over = True
#         elif hard_attempts == 0:
#             print("You've run out of guesses. Refresh the page to run again.")
#             game_over = True
#
# elif game_level == 'easy':
#     while not game_over:
#         guess_num = int(input(f"You have {easy_attempts} attempts remaining to guess the number.\nMake a guess: "))
#         easy_attempts -= 1
#         print(guess_num, computer_num, easy_attempts)
#         compare(computer_num, guess_num)
#
#         if guess_num == computer_num:
#             game_over = True
#         elif easy_attempts == 0:
#             print("You've run out of guesses. Refresh the page to run again.")
#             game_over = True




