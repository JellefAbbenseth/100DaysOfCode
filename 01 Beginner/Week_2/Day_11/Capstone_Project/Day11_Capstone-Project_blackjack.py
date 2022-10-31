# ************ Our Blackjack House Rules ************

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random

from Capstone_Project.art import logo
from replit import clear


def get_card(card_hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    if random_card == 11 and sum(card_hand) + random_card > 21:
        random_card = 1
    return random_card


def play_blackjack():
    print(logo)
    player_cards = []
    dealer_cards = []

    print("Welcome to blackjack!")
    for i in range(2):
        player_cards.append(get_card(player_cards))
        dealer_cards.append(get_card(dealer_cards))

    print(f"Dealer hand: {dealer_cards[0]}, covert")
    print(f"Your hand: {player_cards[0]}, {player_cards[1]}")

    if sum(player_cards) < 21:
        while sum(player_cards) < 21 and input('\nDo you want to get another card? "y" or "n": ') == "y":
            player_cards.append(get_card(player_cards))
            print(f"Your hand sum: {sum(player_cards)}")

        if sum(player_cards) < 21:
            while sum(dealer_cards) < 17:
                dealer_cards.append(get_card(dealer_cards))
        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)

        print(f"Dealer hand sum: {dealer_sum}")
        print(f"Your hand sum: {player_sum}")

        if player_sum > 21:
            print(f"What bad luck, you bust! You lose the game!")
        elif player_sum == 21 or dealer_sum > 21 or player_sum > dealer_sum:
            print("You won the game!")
        elif player_sum == dealer_sum:
            print("A tie!")
        else:
            print("Dealer won the game! You lose the game!")

    elif sum(player_cards) == 21:
        print("You have a Blackjack! What a luck. You won the game!")
    else:
        print("What bad luck, you bust at the Start of the game!\n")

    if input('Do you want to play again. Type "restart".: ') == "restart":
        clear()
        play_blackjack()


play_blackjack()
