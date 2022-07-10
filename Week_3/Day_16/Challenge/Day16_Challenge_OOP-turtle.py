from turtle import Turtle, Screen
from prettytable import PrettyTable

# Timmy the turtle
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("light green")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Pokemon table
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
