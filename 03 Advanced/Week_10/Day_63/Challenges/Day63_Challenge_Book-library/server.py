from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class EditForm(FlaskForm):
    rating = StringField(label='', validators=[DataRequired()])
    submit = SubmitField(label='Change Rating')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Books %r>' % self.title


with app.app_context():
    db.create_all()


def load_books():
    with app.app_context():
        books = db.session.query(Book).all()
    return books


def load_book_by_id(book_id):
    with app.app_context():
        book = db.session.query(Book).filter(Book.id == book_id)[0]
        return book


def add_book(title, author, rating=float):
    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()


def update_book_rating(book_id, new_rating):
    with app.app_context():
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = float(new_rating)
        db.session.commit()


def delete_book_by_id(book_id):
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()


@app.route('/')
def home():
    all_books = load_books()
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


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit(id):
    book = load_book_by_id(id)
    form = EditForm()
    if form.validate_on_submit():
        new_rating = form.rating.data
        update_book_rating(book.id, new_rating)
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, book=book)


@app.route("/delete/<id>")
def delete(id):
    delete_book_by_id(id)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
