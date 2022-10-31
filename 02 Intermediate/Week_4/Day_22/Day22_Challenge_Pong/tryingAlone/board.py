from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.segment import Segment


SCORE_POSITION_ONE = (-40, 220)
SCORE_POSITION_TWO = (40, 220)
ALIGNMENT = "center"
FONT = ("Courier", 34, "bold")


class Board(Segment):
    def __init__(self):
        super().__init__()
        self.board = self.segment
        self.board.hideturtle()
        self.board.pencolor("white")
        self.score_one = 0
        self.score_two = 0

    def write_score(self):
        self.board.clear()
        self.board.goto(SCORE_POSITION_ONE)
        self.board.write(f"{self.score_one}", align=ALIGNMENT, font=FONT)
        self.board.goto(SCORE_POSITION_TWO)
        self.board.write(f"{self.score_two}", align=ALIGNMENT, font=FONT)

    def increase_score(self, side):
        if side == "left":
            self.score_two += 1
        elif side == "right":
            self.score_one += 1
        dif = self.score_one - self.score_two
        if dif >= 2 or dif <= -2:
            self.write_score()
            return False
        return True

    def game_over(self):
        self.board.goto(0, 0)
        self.board.write(f"Game ends! Winner decided!", align=ALIGNMENT, font=FONT)
