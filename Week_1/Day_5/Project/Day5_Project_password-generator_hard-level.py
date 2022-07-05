# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
characters = [letters, numbers, symbols]
choices = [0, 1, 2]
choice = 0
password = ''
sum_password_letters = nr_letters + nr_symbols + nr_numbers
if nr_letters <= 0:
    choices.remove(0)
if nr_numbers <= 0:
    choices.remove(1)
if nr_symbols <= 0:
    choices.remove(2)
if sum_password_letters <= 0:
    print("How funny, you don't want a password")
    quit()
for i in range(0, sum_password_letters):
    choice = random.choice(choices)
    if choice == 0:
        nr_letters -= 1
        if nr_letters <= 0:
            choices.remove(0)
    if choice == 1:
        nr_numbers -= 1
        if nr_numbers <= 0:
            choices.remove(1)
    if choice == 2:
        nr_symbols -= 1
        if nr_symbols <= 0:
            choices.remove(2)
    password += random.choice(characters[choice])

print(f"Here is your password: {password}")
