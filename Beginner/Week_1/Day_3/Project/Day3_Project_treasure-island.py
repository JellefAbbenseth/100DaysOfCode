print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
choice = input('On your left side is a bridge, do you want to go "right" or "left"\n')
if choice.lower() == "left":
    choice = input('There is an orc, who asks you:\n'
                   '"What has four legs in the morning, two at noon and three in the evening"\n'
                   'What do you answer?\n')
    if choice.lower() == "human":
        choice = input('The orc is happy so he let you pass over the bridge.\n'
                       'You find yourself in front of an old castle.\n'
                       'Do you want to go through the front door "straight", "left" or "right"?\n')
        if choice.lower() == "right":
            print("You got lucky,"
                  " you found a small hole and got into the old castle to find a small diamond in a chest.")
        elif choice.lower() == "straight":
            print("Bad choice, there is a group of orcs, so you get yourself killed.")
        elif choice.lower() == "left":
            print("You didn't find anything good, therefore you took all the trouble for nothing. You loose!")
        else:
            print("So you went back, because the orc isn't amused about your choice, he kills you!")
    else:
        print("The orc kills you!")
else:
    print("You walk into a forest and got stuck, without a way back! You starve to death!")
