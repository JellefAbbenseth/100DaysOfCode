from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Books %r>' % self.title


with app.app_context():
    db.create_all()

all_books = []


def add_book(title=str, author=str, rating=float):
    all_books.append(
        {
            "title": title,
            "author": author,
            "rating": rating,
        }
    )
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()


def load_books():
    with app.app_context():
        books = db.session.query(Book).all()
    print(books[0])


load_books()


@app.route('/')
def home():
    return render_template('index.html', book_list=all_books)


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/add_data", methods=['GET', 'POST'])
def add_data():
    title = request.form['bookname']
    author = request.form['author']
    rating = request.form['rating']
    add_book(title, author, float(rating))

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
