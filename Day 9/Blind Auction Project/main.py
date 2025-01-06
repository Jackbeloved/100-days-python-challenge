# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
print("Welcome to the secret auction program.")

bid_list ={}
keep = True
while keep:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bid_list[name] = bid
    end = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if end == "no":
        keep = False
        print("\n" * 100)
    else:
        keep = True
        print("\n"*100)

# print(f"list is {bid_list}")
name_list = []
num_list = []
bid_name =""
bid_price =""
for i in bid_list:
    num_list.append(bid_list[i])
    if bid_list[i] == max(num_list):
        bid_name = i
        bid_price = max(num_list)
print(f"The winner is {bid_name} with a bid of {bid_price}")

