from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def write_level(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT )

    def increase_level(self):
        self.level += 1

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!", align=ALIGNMENT, font=FONT)
