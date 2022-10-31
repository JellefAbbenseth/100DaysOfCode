from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.segment import Segment

BORDER = 260
START_POS_X = 560
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Character:
    def __init__(self, start_point):
        self.start_point = start_point
        self.positions = self.create_positions()
        self.segments = []
        self.create_player()
        self.leading = self.segments[0]
        self.leading.setheading(UP)

    def create_player(self):
        for position in self.positions:
            segment = Segment(position)
            self.segments.append(segment.segment)

    def create_positions(self):
        pos_x = START_POS_X
        if self.start_point.lower() == "left":
            pos_x = -START_POS_X
        return [(pos_x, 40), (pos_x, 20), (pos_x, 0), (pos_x, -20), (pos_x, -40)]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.leading.forward(MOVE_DISTANCE)

    def flip(self):
        for i in range(len(self.segments) - 1):
            self.move()

    def up(self):
        if self.leading.ycor() <= BORDER:
            if self.leading.heading() == DOWN:
                self.leading.setheading(UP)
                self.flip()
            self.move()

    def down(self):
        if self.leading.ycor() >= -BORDER:
            if self.leading.heading() == UP:
                self.leading.setheading(DOWN)
                self.flip()
            self.move()
