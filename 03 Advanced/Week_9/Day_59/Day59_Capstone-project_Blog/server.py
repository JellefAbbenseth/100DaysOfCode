import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def home():
    blog_url = "https://api.npoint.io/528fc9ab5652e1299bc3"
    all_posts = requests.get(blog_url).json()
    return render_template('index.html', posts=all_posts)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/post/<num>')
def get_post(num):
    blog_url = "https://api.npoint.io/528fc9ab5652e1299bc3"
    all_posts = requests.get(blog_url).json()
    return render_template('post.html', posts=all_posts, id=int(num))


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
