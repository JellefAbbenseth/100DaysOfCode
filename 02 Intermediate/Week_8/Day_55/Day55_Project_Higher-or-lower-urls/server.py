import random

from flask import Flask

random_number = random.randrange(0, 10)
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media0.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid" \
           "=ecf05e47fc494ldeh6yjhmxasf930x1ulocen75o3uuhs9nz&rid=giphy.gif&ct=g'" \
           "alt='number-guessing-gif'>"


def add_info(function):
    def wrapper_function(*args, **kwargs):
        result = int(function(kwargs)['number'])
        if result == random_number:
            return "<h1 style='color: green;'>You found me!</h1><img " \
                   "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='correct-gif'> "
        elif result > random_number:
            return "<h1 style='color: violet;'>Too high, try again!</h1><img " \
                   "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='too-high-gif'> "
        elif result < random_number:
            return "<h1 style='color: red;'>Too low, try again!</h1><img " \
                   "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='too-low-gif'> "

    return wrapper_function


@app.route("/<int:number>")
@add_info
def greet(number):
    return number


if __name__ == "__main__":
    app.run(debug=True)
