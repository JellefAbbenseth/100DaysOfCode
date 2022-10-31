from turtle import Turtle

STARTING_POSITION_Y = 0
MOVE_DISTANE = 20


class Snake:
    def __init__(self):
        pos_x = 0
        self.segments = []
        for i in range(3):
            self.new_segment(pos_x)
            pos_x -= 20

    def new_segment(self, x):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x, STARTING_POSITION_Y)
        self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANE)
