from data import *

money = 0.0


def show_report():
    print(f"""Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}""")
    print("Money: $%.2f" % money)


def check_resources(coffee_choice):
    missing_resource = ""

    for resource in resources:
        if coffee_choice == "espresso" and resource == "milk":
            continue
        if MENU[coffee_choice]["ingredients"][resource] > resources[resource]:
            missing_resource = resource

    if missing_resource == "":
        return True
    print(f"Sorry there is not enough {missing_resource}.\n")
    return False


def calculate_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)


def calculate_change(coffee, given_money):
    return round(given_money - MENU[coffee]["cost"], 2)


def make_coffee(coffee, money_change):
    print(f"Here is ${money_change} dollars in change.")
    print(f"Here is your {coffee}. Enjoy!")
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        print("Coffee machine turning off. Good bye!")
        exit()
    elif user_choice == "report":
        show_report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        enough_resources = check_resources(user_choice)
        if enough_resources:
            print(f"Please insert coins.")
            money = calculate_coins()
            change = calculate_change(user_choice, money)
            if change >= 0:
                make_coffee(user_choice, change)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Wrong entry, please choose again!\n")
