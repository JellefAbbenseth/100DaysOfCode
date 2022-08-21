import random
import turtle

import colorgram

rgb_colors = []
colors = colorgram.extract('image_circle.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)


# ***** get the colors as tuple array

def to_color_tuple(rgb_color):
    color_tuple = (rgb_color.r, rgb_color.g, rgb_color.b)
    return color_tuple


color_array = []
for color in rgb_colors:
    color_array.append(to_color_tuple(color))

print(color_array)

# original: [(250, 248, 237), (237, 250, 244), (251, 239, 246), (232, 242, 249), (199, 158, 111), (227, 220, 102),
# (145, 88, 53), (43, 109, 148), (121, 170, 194), (159, 17, 56), (198, 140, 161), (10, 30, 63), (156, 59, 89), (54,
# 25, 13), (131, 179, 149), (170, 157, 42), (67, 12, 39), (52, 125, 74), (205, 76, 109), (9, 39, 20), (214, 88, 60),
# (229, 168, 189), (80, 161, 102), (135, 32, 22), (42, 160, 191), (18, 95, 50), (163, 210, 181), (30, 53, 113), (221,
# 222, 12), (149, 209, 221)]
#
# usable: [(199, 158, 111), (227, 220, 102), (145, 88, 53), (43, 109, 148), (121, 170,
# 194), (159, 17, 56), (198, 140, 161), (10, 30, 63), (156, 59, 89), (54, 25, 13), (131, 179, 149), (170, 157, 42),
# (67, 12, 39), (52, 125, 74), (205, 76, 109), (9, 39, 20), (214, 88, 60), (229, 168, 189), (80, 161, 102), (135, 32,
# 22), (42, 160, 191), (18, 95, 50), (163, 210, 181), (30, 53, 113), (221, 222, 12), (149, 209, 221)]

usable_color_array = []

for i in range(4, len(color_array)):
    usable_color_array.append(color_array[i])

print(usable_color_array)

pain = turtle.Turtle()
turtle.colormode(255)
pain.hideturtle()
pain.penup()
posx = -200
posy = -200
pain.goto(posx, posy)
pain.shape("arrow")
pain.color("black")
length = 10
height = 10
dot_weight = 20
way_length = 2 * dot_weight
for i in range(length):
    for j in range(height):
        pain.dot(dot_weight, random.choice(color_array))
        pain.forward(way_length)
    posy += way_length
    pain.goto(posx, posy)

screen = turtle.Screen()
screen.exitonclick()
