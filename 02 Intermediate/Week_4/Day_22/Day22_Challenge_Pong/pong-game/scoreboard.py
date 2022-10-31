from turtle import Turtle
from global_variables import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner = ""

    def write_score(self):
        self.clear()
        self.goto(-SCORE_X_POS, SCORE_Y_POS)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(SCORE_X_POS, SCORE_Y_POS)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def write_winner(self):
        self.goto(0, 0)
        self.write(f"The winner is on the {self.winner}!", align=ALIGNMENT, font=FONT_WINNER)

    def add_r(self):
        self.r_score += 1

    def add_l(self):
        self.l_score += 1

    def end_game(self):
        if self.r_score - self.l_score > 2:
            self.winner = "right"
            return False
        elif self.r_score - self.l_score < -2:
            self.winner = "left"
            return False
        return True
