from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")
NUMBER_STATES = 50


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("black")
        self.penup()
        self.count_states = 0

    def write_state(self, position, state_name):
        self.count_states += 1
        self.goto(position)
        self.write(f"{state_name}", align=ALIGNMENT, font=FONT)
