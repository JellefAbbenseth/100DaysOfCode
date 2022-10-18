import random
import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = datetime.date.today().year
    user_name = "Your_name"  # input("Please tell us your name: ")
    return render_template('index.html', num=random_number, year=current_year, name=user_name)


if __name__ == "__main__":
    app.run(debug=True)
