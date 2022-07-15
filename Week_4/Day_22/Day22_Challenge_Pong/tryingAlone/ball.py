import random

from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.segment import Segment

UPPER_BOUNDARY = 290
RIGHT_BOUNDARY = 590

MOVE_DISTANCE = 10
RIGHT = 0
UP = 90
FLIP = 180


class Ball(Segment):
    def __init__(self):
        super().__init__(self.random_position())
        self.direction_up = UP
        self.direction_right = RIGHT

    def random_position(self):
        position = (random.randint(-250, 250), random.randint(-250, 250))
        return position

    def move(self):
        self.segment.setheading(self.direction_up)
        self.segment.forward(MOVE_DISTANCE)
        self.segment.setheading(self.direction_right)
        self.segment.forward(MOVE_DISTANCE)

    def refresh(self):
        self.segment.hideturtle()
        self.segment.goto(self.random_position())
        self.segment.showturtle()

    def change_direction(self):
        position = self.segment.position()

        if position[1] >= UPPER_BOUNDARY or position[1] <= -UPPER_BOUNDARY:
            self.direction_up += FLIP
        if position[0] >= RIGHT_BOUNDARY or position[0] <= -RIGHT_BOUNDARY:
            self.direction_right += FLIP
            self.refresh()
