from turtle import Turtle
from global_variables import *


class Paddle(Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.position()[1] <= BORDER_Y_PADDLE:
            new_y = self.ycor() + STEPS
            self.goto(self.xcor(), new_y)
            # paddle_right.setheading(UP)
            # paddle_right.forward(STEPS)
            # paddle_right.setheading(RIGHT)

    def down(self):
        if -BORDER_Y_PADDLE <= self.position()[1]:
            new_y = self.ycor() - STEPS
            self.goto(self.xcor(), new_y)
