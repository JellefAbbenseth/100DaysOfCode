# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name = (name1 + name2).lower()

counter_true = name.count("t")
counter_true += name.count("r")
counter_true += name.count("u")
counter_true += name.count("e")
# print(counter_true)
counter_love = name.count("l")
counter_love += name.count("o")
counter_love += name.count("v")
counter_love += name.count("e")
# print(counter_love)
counter = int(str(counter_true) + str(counter_love))
# print(counter)
if counter < 10 or counter > 90:
    print(f"Your score is {counter}, you go together like coke and mentos.")
elif 40 < counter < 50:
    print(f"Your score is {counter}, you are alright together.")
else:
    print(f"Your score is {counter}.")
