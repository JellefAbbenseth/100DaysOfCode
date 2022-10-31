# Guess a number game
# difficulties attempts:
#  - hard: 5
#  - easy: 10
import random

from Project.art import *

print(logo)
attempts = 10
word = "attempts"
won = False
if input('Choose a difficulty. Type "easy" or "hard": ') == "hard":
    attempts = 5

secret_num = random.randint(0, 100)

while attempts > 0 and won is False:
    if attempts == 1:
        word = "attempt"
    print(f"You have {attempts} {word} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == secret_num:
        won = True
    elif guess > secret_num:
        print("Too high.")
        attempts -= 1
    else:
        print("Too low.")
        attempts -= 1

if not won:
    print(f"You've run out of guesses!\n{lose_logo}")
else:
    print(f"Congratulation you guessed correct!\n{win_logo}")
