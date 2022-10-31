from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.segment import Segment

BORDER = 300
MOVING_DISTANCE = 20
START_LINE_POSITION = (0, BORDER)
ALIGNMENT = "center"
FONT = ("Courier", 34, "bold")


class Field(Segment):
    def __init__(self):
        super().__init__()
        self.board = self.segment
        self.board.hideturtle()
        self.board.pencolor("white")
        self.board.setheading(270)

    def write_line(self):
        self.board.goto(START_LINE_POSITION)
        while self.board.ycor() >= -BORDER:
            self.board.pendown()
            self.board.forward(MOVING_DISTANCE)
            self.board.penup()
            self.board.forward(MOVING_DISTANCE)
