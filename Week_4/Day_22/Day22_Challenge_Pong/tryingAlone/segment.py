from turtle import Turtle


class Segment:
    def __init__(self, position=(0, 0)):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.segment = square
