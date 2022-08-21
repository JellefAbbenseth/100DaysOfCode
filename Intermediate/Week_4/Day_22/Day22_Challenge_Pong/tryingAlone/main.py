import time
from turtle import Screen

from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.ball import Ball
from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.character import Character
from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.board import Board
from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.field import Field

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
game_is_on = True
score = 0


def end_game():
    global game_is_on
    game_is_on = False


def check_player_ball_collision(player):
    global game_is_on
    for segment in player.segments:
        if ball.segment.distance(segment) < 20:
            return True
    return False


board = Board()
field = Field()
field.write_line()
ball = Ball()
player_1 = Character("right")
player_2 = Character("left")

screen.listen()
screen.onkey(key="e", fun=end_game)
screen.onkeypress(key="w", fun=player_2.up)
screen.onkeypress(key="s", fun=player_2.down)
screen.onkeypress(key="Up", fun=player_1.up)
screen.onkeypress(key="Down", fun=player_1.down)

while game_is_on:
    screen.update()
    ball.move()
    board.write_score()
    time.sleep(0.1)

    # Detect player missing ball
    player_misses = ball.change_direction()
    game_is_on = board.increase_score(player_misses)

    # Detect collision with player
    if check_player_ball_collision(player_1) or check_player_ball_collision(player_2):
        ball.change_direction(True)

time.sleep(1)
board.game_over()
screen.exitonclick()
