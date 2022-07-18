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
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def write_score(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()
