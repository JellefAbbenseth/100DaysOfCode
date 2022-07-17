import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)
game_is_on = True


def end_game():
    global game_is_on
    game_is_on = False


player = Player()
scoreboard = Scoreboard()
cars = []
for i in range(30, 51):
    cars.append(CarManager())

screen.listen()
screen.onkeypress(key="Up", fun=player.moving)
screen.onkey(key="e", fun=end_game)

while game_is_on:
    scoreboard.write_level()
    time.sleep(0.1)
    screen.update()

    # Check collision
    for car in cars:
        car.moving()
        if player.distance(car.xcor(), car.ycor()) <= 20:
            game_is_on = False

    # Check player reaching finishing line
    level_up = player.end_reached()
    if level_up:
        for car in cars:
            car.increase_speed()
        scoreboard.increase_level()
        player.reset()

time.sleep(1)
scoreboard.write_game_over()
screen.exitonclick()
