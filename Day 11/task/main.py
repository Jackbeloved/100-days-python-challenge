import random

import art
play_game = input("Do you want to play a game of Blackjack?")
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
dealer_cards=[]
your_score = 0


def your_cards_on_hand():
    for loop in range(2):
        your_cards.append(random.choice(card_list))
    return print(your_cards)
your_cards_on_hand()

def dealer_cards_on_hand():
    for loop in range(2):
        dealer_cards.append(random.choice(card_list))
    return print(dealer_cards)
dealer_cards_on_hand()

def compare(your_total,dealer_total):
    if your_total > 21:
        print("You went over. You lose")
    elif dealer_total > 21:
        print("You win.")
    elif your_total > dealer_total:
        print("You win")
    elif your_total == dealer_total:
        print("Draw")
    else:
        print("You lose")

# def check_total(user,computer):
#     if user == 21:
#         print("win")
#     elif computer ==21:
#         print("lose")
#     elif user > 21:
#         if 11 in user:
#             if (user - 10) >21:
#                 print("lose")
#             else:
#                 user = user-10
#         else:
#             print("lose")
#



if play_game =="y":
    print("\n"*20)
    print(art.logo)
    continue_play = True
    while continue_play:
        your_score = sum(your_cards)
        print(dealer_cards,sum(dealer_cards))
        print(f"Your cards: {your_cards}, current score: {your_score}\n"
              f"Computer's first card : {dealer_cards[0]}")
        another_card = input("Type 'y' to get another card, type y'n' to pass")
        if another_card =="y":

            continue_play = True

        else:
            continue_play = False


            # your_cards.append(random.choice(card_list))
            # dealer_cards.append(random.choice(card_list))
            #
            # print(f"hey hey{your_cards}")

