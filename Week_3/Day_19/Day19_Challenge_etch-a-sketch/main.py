from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Make an Etch-A-Sketch App
# W = Forwards
# S = Backwards
# A = Counter-Clockwise
# D = Clockwise


def clear_game():
    tim.reset()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


screen.listen()
screen.onkey(key="c", fun=clear_game)
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=counter_clockwise)

screen.exitonclick()
