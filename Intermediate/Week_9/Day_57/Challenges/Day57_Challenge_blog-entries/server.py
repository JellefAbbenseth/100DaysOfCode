import random, datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = datetime.date.today().year
    user_name = "Your_name"  # input("Please tell us your name: ")
    return render_template('index.html', num=random_number, year=current_year, name=user_name)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
