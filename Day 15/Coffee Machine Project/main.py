from operator import truediv
from platform import machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO:4.CHECK RESOURCES FOR EACH ORDER
def check_resource():
    if customer_choice =="espresso":
        if water >= water_cost and coffee >= coffee_cost:
            return True
        elif water < water_cost:
            print("not enough water")
        elif coffee < coffee_cost:
            print("not enough coffee")
    else:
        if water >= water_cost and milk >= milk_cost and coffee >= coffee_cost:
            return True
        elif water < water_cost:
            print("not enough water")
        elif milk < milk_cost:
            print("not enough milk")
        elif coffee < coffee_cost:
            print("not enough coffee")

#TODO:5.PROCESS COIN
def calculate_coin():
    print("insert coin")
    quarters_count = int(input("how many quarters?"))* 0.25
    dimes_count = int(input("how many dimes?")) * 0.10
    nickles_count = int(input("how many nickles?")) * 0.05
    pennies_count = int(input("how many pennies?")) * 0.01
    coin_total = round(quarters_count + dimes_count + nickles_count + pennies_count,2)
    return coin_total

# TODO:6.CHECK TRANSACTION
def transaction():
    change = round(payment - order_cost, 2)
    if change >= 0:
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry not enough money")
        return False

#TODO:7.MAKE COFFEE
# def make_coffee():
#     water -= water_cost
#     milk -= milk_cost
#     coffee -= coffee_cost
#     money += order_cost

machine_off = False
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
# print(water, milk, coffee)
money = 0


while not machine_off:
    #TODO:1.Ask user what they like
    customer_choice = input("What would you like(espresso/latte/cappuccino)\n").lower()
    #TODO:2.INPUT OFF TO TURN OFF PROGRAM
    if customer_choice == "off":
        machine_off = True
    #TODO:3.PRINT REPORT
    elif customer_choice == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    else:
        water_cost = MENU[customer_choice]["ingredients"]["water"]
        coffee_cost = MENU[customer_choice]["ingredients"]["coffee"]
        if customer_choice == "espresso":
            milk_cost = 0
        else:
            milk_cost = MENU[customer_choice]["ingredients"]["milk"]
        # print(water_cost, milk_cost, coffee_cost)

        order_cost = MENU[customer_choice]["cost"]
        # print(order_cost)
        payment = calculate_coin()

        if check_resource() and transaction():
            water -= water_cost
            milk -= milk_cost
            coffee -= coffee_cost
            money += order_cost
            print(water,milk,coffee,money)
            print(f"enjoy your {customer_choice} ")



