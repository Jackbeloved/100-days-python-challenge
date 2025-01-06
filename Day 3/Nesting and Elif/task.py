print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
photo = input("yes or no?")
if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        bill = 5
        print("5")
    elif age >12 and age <= 18:
        bill =12
        print("12")
    else:
        bill =18
        print("18")
    if photo == "yes":
        bill+=3
    print(f"total = {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
