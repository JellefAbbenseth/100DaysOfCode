from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        self.finish_line_reached = False

    def moving(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.finish_line_reached = True
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.finish_line_reached = False
        self.goto(STARTING_POSITION)

    def end_reached(self):
        return self.finish_line_reached
