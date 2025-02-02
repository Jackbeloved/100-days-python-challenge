#TO DO LIST
#1.IMPORT LOGO

from art import logo,vs

print(logo)
#2.PICK 2 RANDOM DATA FROM GAME DATA
from game_data import data
import random

def object_select():
    number = random.randint(0,len(data)-1)
    return data[number]
account_b = object_select()

score =0
game_over = False
while not game_over:
    account_a =account_b
    account_b = object_select()
    if account_b == account_a:
        account_b = object_select()
    print(account_a,account_b)

    def acct_info(acct_detail):
        return f"{acct_detail['name']}, {acct_detail['description']}, from {acct_detail['country']}"

    print(acct_info(account_a))
    print(acct_info(account_b))

    def compare(guess,a_fans,b_fans):
        if  a_fans > b_fans and guess == "a":
           return  True
        elif  a_fans < b_fans and guess == "b":
           return  True
        else:
            return False

    print(f"Compare A: {acct_info(account_a)}")
    print(vs)
    print(f"Compare B: {acct_info(account_b)}")

    choice = input("Who has more followers? Type 'A' or 'B':").lower()

    a_follower = account_a['follower_count']
    print(a_follower)
    b_follower = account_b['follower_count']
    print(b_follower)
    pass_game = compare(choice,a_follower,b_follower)
    print(pass_game)

    if pass_game:
                score += 1
                print(f"You're right! Current score: {score}.")
                game_over = False

    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True



# # print("\n" * 100)
# # print(winner)
# score = 0
# game_over = False
# while not game_over:
#
#     # a_info = object_select()
#     print(f"Compare A: {a_info['name']}, {a_info['description']}, from {a_info['country']}")
#     a_follower = a_info['follower_count']
#     #
#     # print(art.vs)
#     #
#     # b_info = object_select()
#     print(f"Compare B: {b_info['name']}, {b_info['description']}, from {b_info['country']}")
#     b_follower = b_info['follower_count']
#     winner = compare(a_follower, b_follower)
#     # print(winner)
#     choice = input("Who has more followers? Type 'A' or 'B':").lower()
#     #
#     # print("\n" * 100)
#
#     if choice ==  winner:
#         score += 1
#         print(logo)
#         print(f"You're right! Current score: {score}.")
#         a_info = b_info
#         print(a_info)
#         b_info = object_select()
#         print(b_info)
#         game_over = False
#
#
#     else:
#         print(logo)
#         print(f"Sorry, that's wrong. Final score: {score}")
#         game_over = True



#3. IF RIGHT PUT B TO A AND GET NEW B