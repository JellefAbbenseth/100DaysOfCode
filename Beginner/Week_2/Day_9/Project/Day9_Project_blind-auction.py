from Project.art import logo
from replit import clear

# HINT: You can call clear() to clear the output in the console.

global bidder
bidder = {}


def add_bidder(name, bid):
    bidder[name] = bid


def highest_bidder():
    highest_bid = 0
    highest_bid_key = ""
    for key in bidder:
        if bidder[key] > highest_bid:
            highest_bid = bidder[key]
            highest_bid_key = key
    return highest_bid_key


print(logo + "\nWelcome to the secret auction program.")
choice = "yes"
while choice == "yes":
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bidder(name, bid)
    choice = input('Are there any other bidders? Type "yes" or "no". ')
    clear()

print(f"Congratulation {highest_bidder()}, for the highest bid with ${bidder[highest_bidder()]}.")
