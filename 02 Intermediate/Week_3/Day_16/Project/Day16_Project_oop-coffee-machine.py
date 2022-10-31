from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
menu_items = menu.get_items().split("/")
money_machine = MoneyMachine()

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input.lower() in menu_items:
        drink_item = menu.find_drink(user_input)
        drink_possible = coffee_maker.is_resource_sufficient(drink_item)
        if drink_possible:
            payment_sufficient = money_machine.make_payment(drink_item.cost)
            if payment_sufficient:
                coffee_maker.make_coffee(drink_item)
        else:
            print("Sorry there is not enough water.\n")
    elif user_input.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input.lower() == "off":
        print("The Machine will shut down. Have a nice day.")
        exit()
    else:
        print("Wrong input, please try again!\n")
