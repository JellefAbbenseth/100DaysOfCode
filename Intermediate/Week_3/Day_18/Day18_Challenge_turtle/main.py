# ****Turtle Intro****
import random
import turtle
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.penup()
tim.left(90)
tim.forward(250)
tim.right(90)
tim.pendown()
tim.forward(100)
tim.backward(200)
tim.right(90)
tim.left(180)
tim.setheading(0)
t.colormode(255)


# ****** Challenge 1 - Draw a Square *******

tim.color("blue")
for i in range(4):
    tim.forward(100)
    tim.left(90)

# ****** Challenge 2 - Draw a Dashed Line *******
tim.right(90)
for i in range(15):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

# ****** Challenge 3 - Draw different shapes *******
color = []
n = 100
for i in range(n):
    color.append('#%06X' % random.randint(0, 0xFFFFFF))

tim.left(90)
amount_corners = 3
side_length = 100
amount_different_shapes = 10
for i in range(amount_different_shapes):
    for j in range(amount_corners):
        tim.forward(side_length)
        tim.right(360 / amount_corners)
    amount_corners += 1
    tim.pencolor(random.choice(color))

# ****** Challenge 4 - Draw a Random Walk *******
t.resetscreen()
amount_actions = 200
tim.speed(10)
tim.pensize(10)
directions = [0, 90, 180, 270]

for i in range(amount_actions):
    tim.color(random.choice(color))
    tim.setheading(random.choice(directions))
    tim.forward(20)

# ****** Challenge 5 - Draw random colours *******
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


t.resetscreen()
amount_actions = 200
tim.speed(10)
tim.pensize(10)
directions = [0, 90, 180, 270]

for i in range(amount_actions):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(20)

# ****** Challenge 6 - Draw a Spirograph *******
t.resetscreen()
tim.speed(20)
tim.pensize(1)
r = 100
degree = 5
for i in range(0, int(round(360 / degree, 0))):
    tim.circle(r)
    tim.right(degree)
    tim.color(random_color())

screen = t.Screen()
screen.exitonclick()
