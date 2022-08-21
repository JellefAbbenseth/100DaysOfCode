import random

from Project.game_data import data
from Project.art import *
from replit import clear

player_continues = True
player_score = 0


def get_random_data():
    return random.choice(data)


def print_star_data(star_data):
    return f"{star_data['name']}, a {star_data['description']}, from {star_data['country']}."


data_a = get_random_data()
print(logo)

while player_continues:
    data_b = data_a
    while data_b == data_a:
        data_b = get_random_data()

    print(f"Compare A: {print_star_data(data_a)}")
    print(vs)
    user_choice = input(
        f"Against B: {print_star_data(data_b)}\nWho has more followers? "
        f"Type 'A' or 'B': ").upper()

    if user_choice == 'B' and data_b['follower_count'] > data_a['follower_count'] or \
            user_choice == 'A' and data_a['follower_count'] > data_b['follower_count']:
        player_score += 1
        data_a = data_b
        clear()
        print(logo)
        print(f"You're right! Current score: {player_score}.")
    else:
        player_continues = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. final score: {player_score}.")
