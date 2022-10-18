import requests

from flask import Flask, render_template

app = Flask(__name__)


def get_gender(name: str):
    genderize_endpoint = "https://api.genderize.io"
    user_params = {
        "name": name,
    }
    response = requests.get(url=genderize_endpoint, params=user_params).json()
    return response["gender"]


def get_age(name: str):
    agify_endpoint = "https://api.agify.io"
    user_params = {
        "name": name,
    }
    response = requests.get(url=agify_endpoint, params=user_params).json()
    return response["age"]


@app.route('/guess/<name>')
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template('index.html', name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
