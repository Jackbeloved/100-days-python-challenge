# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def greet_with(name,location):
#     print(f"hi{name}")
#     print(f"loca {location}")
#
# greet_with(name="ja",location="h")
def calculate_love_score(name1, name2):
    count_true = 0
    word_list = ["TRUE", "LOVE"]

    for letter in name1.upper():
        if letter in word_list[0]:
            count_true += 1

    for letter in name2.upper():
        if letter in word_list[0]:
            count_true += 1

    count_love = 0
    for letter in name1.upper():
        if letter in word_list[1]:
            count_love += 1
    for letter in name2.upper():
        if letter in word_list[1]:
            count_love += 1
    print(count_true,count_love)

calculate_love_score("Angela Yu", "Jack Bauer")