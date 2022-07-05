import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

# Write your code below this line 👇

hands = [rock, paper, scissors]

player_choice = hands[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))]
print(player_choice)
computer_choice = random.choice(hands)
print("Computer chose:\n" + computer_choice)

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == hands[0] and computer_choice == hands[2] or\
        player_choice == hands[2] and computer_choice == hands[1] or\
        player_choice == hands[1] and computer_choice == hands[0]:
    print("You win!")
else:
    print("You lose!")

