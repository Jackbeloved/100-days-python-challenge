import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(list):
    """calculate total score"""
    if len(list) == 2 and sum(list) == 21:
        return 0
    elif 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
        return sum(list)
    else:
        return sum(list)

def deal_card():
    """return random card"""
    return  random.choice(cards)



play_game = input("Do you want to play a game of Blackjack?")
user_cards = []
computer_cards = []

if play_game == "y":
    print(art.logo)

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards},current score: {user_score}\nComputer card: {computer_cards[0]}")
    print({computer_cards},{computer_score})

    game_over = False
    while game_over is False:
        if user_score == 0 or computer_score ==0 or user_score >21:
            game_over = True

        else:
            another_card = input("Type 'y' to get another card, type y'n' to pass")
            if another_card == "y":
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards},current score: {user_score}\nComputer card: {computer_cards[0]}")
                print({computer_cards},{computer_score})
    if user_score == 0:
        print("win")
    elif computer_score ==0 or user_score >21:
        print("lose")



