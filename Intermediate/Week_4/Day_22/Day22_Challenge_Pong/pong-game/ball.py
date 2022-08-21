from turtle import Turtle
from global_variables import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x_move = STEPS_X
        self.y_move = STEPS_Y
        self.ball_speed = 1

    def move(self):
        if self.ycor() <= -BORDER_Y_BALL or self.ycor() >= BORDER_Y_BALL:
            self.bounce_y()
        new_x = self.xcor() + self.x_move * self.ball_speed
        new_y = self.ycor() + self.y_move * self.ball_speed
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.bounce_y()
        self.ball_speed = 1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.ball_speed += 0.1
