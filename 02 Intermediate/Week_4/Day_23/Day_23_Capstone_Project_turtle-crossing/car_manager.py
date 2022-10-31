import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.setheading(LEFT)
        self.color(random.choice(COLORS))
        self.goto(random.randint(-300, 950), random.randint(-240, 240))
        self.multiplier = 0

    def increase_speed(self):
        if self.multiplier == 0:
            self.multiplier += 0.5
        else:
            self.multiplier *= 1.2

    def moving(self):
        if self.xcor() < -400:
            self.starting_point()
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * self.multiplier)

    def starting_point(self):
        self.goto(random.randint(300, 950), random.randint(-240, 240))
