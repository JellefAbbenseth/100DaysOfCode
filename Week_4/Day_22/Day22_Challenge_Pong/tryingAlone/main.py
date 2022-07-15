import time
from turtle import Screen

from Week_4.Day_22.Day22_Challenge_Pong.tryingAlone.ball import Ball

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(key="e", fun=end_game)

ball = Ball()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()
    ball.change_direction()

screen.exitonclick()
