from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"

    return wrapper_function


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Goodbye!'


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
