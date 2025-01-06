import random
#rock paper sciccor

# computer_input = random.randint(1,3)

# print(f"your choice is {your_input} and computer {computer_input}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
your_input= int(input("what 0,1,2\n"))
str_range = [rock,paper,scissors]
computer_choice = random.choice (str_range)


if your_input == 0:
    print(str_range[your_input],f"computer choice {computer_choice}")
    if computer_choice == paper:
        print("you lose")
    elif computer_choice == rock:
        print("draw")
    else:
        print("you win")
elif your_input == 1:
    print(str_range[your_input], f"computer choice {computer_choice}")
    if computer_choice == paper:
            print("draw")
    elif computer_choice == rock:
            print("you win")
    else:
            print("you lose")
elif your_input == 2:
        print(str_range[your_input],f"computer choice {computer_choice}")
        if computer_choice == paper:
            print("you win")
        elif computer_choice == rock:
            print("you lose")
        else:
            print("draw")
else:
    print("wrong")