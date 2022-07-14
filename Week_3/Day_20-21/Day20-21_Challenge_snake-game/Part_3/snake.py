from turtle import Turtle

STARTING_POSITION_Y = 0
MOVE_DISTANE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        pos_x = 0
        self.segments = []
        for i in range(3):
            self.new_segment(pos_x)
            pos_x -= 20
        self.head = self.segments[0]

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
        self.head.forward(MOVE_DISTANE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
