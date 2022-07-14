from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on: bool = True

COORDINATE = 280
DISTANCE = 15


def end_game():
    global game_is_on
    game_is_on = False


snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.write_score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="e", fun=end_game)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < DISTANCE:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.write_score()

    # Detect collision with wall.
    if snake.head.xcor() > COORDINATE or \
            snake.head.xcor() < -COORDINATE or \
            snake.head.ycor() > COORDINATE or \
            snake.head.ycor() < -COORDINATE:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
