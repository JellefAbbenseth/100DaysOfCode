import time

from turtle import Screen
from ball import Ball
from global_variables import *
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False


r_paddle = Paddle((START_POS_X, START_POS_Y))
l_paddle = Paddle((-START_POS_X, START_POS_Y))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)
screen.onkey(key="e", fun=end_game)

while game_is_on:
    screen.update()
    time.sleep(TIME_SLEEP)

    ball.move()
    scoreboard.write_score()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > BORDER_X_BALL or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -BORDER_X_BALL:
        ball.bounce_x()
        ball.increase_speed()

    # Detect paddle misses
    if ball.xcor() <= -BORDER_X_PADDLE:
        scoreboard.add_r()
        ball.reset()
    if ball.xcor() >= BORDER_X_PADDLE:
        scoreboard.add_l()
        ball.reset()

    game_is_on = scoreboard.end_game()

time.sleep(1)
scoreboard.write_winner()
screen.exitonclick()
