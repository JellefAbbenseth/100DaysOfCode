import turtle
from turtle import Turtle

SCORE_POSITION = (0, 260)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.score = 0

    def write_score(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
