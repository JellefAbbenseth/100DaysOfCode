from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import desc
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, URL, length
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


# SQLAlchemy Class

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Movies %r' % self.title


# Database interactions

def add_movie(new_movie):
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()


def load_movies():
    with app.app_context():
        movies = db.session.query(Movie).order_by(desc(Movie.rating)).all()
    return movies


def load_movie_by_id(movie_id):
    with app.app_context():
        movie = db.session.query(Movie).filter(Movie.id == movie_id)[0]
        return movie


def update_movie_by_id(movie_id, new_rating, new_review):
    with app.app_context():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()


def update_movie_ranking_by_id(movie_id, new_ranking):
    with app.app_context():
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.ranking = new_ranking
        db.session.commit()


def delete_movie_by_id(movie_id):
    with app.app_context():
        movie_to_delete = Movie.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()


with app.app_context():
    db.create_all()

    if len(load_movies()) < 1:
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an "
                        "extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation "
                        "with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()


# Formulas
class EditForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired(), length(max=50)])
    year = IntegerField(label='Year', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired(), length(max=250)])
    rating = FloatField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired(), length(max=250)])
    img_url = StringField(label='Image_url', validators=[DataRequired(), URL(), length(max=250)])
    submit = SubmitField(label='Add Movie')


def update_ranking():
    movies = load_movies()
    for i in range(len(movies)):
        update_movie_ranking_by_id(movies[i].id, i+1)


@app.route("/")
def home():
    update_ranking()
    movies = load_movies()
    return render_template("index.html", movies=movies)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        data = Movie(
            title=form.title.data,
            year=form.year.data,
            description=form.description.data,
            rating=form.rating.data,
            ranking=0,
            review=form.review.data,
            img_url=form.img_url.data
        )
        add_movie(new_movie=data)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    movie = load_movie_by_id(movie_id)
    form = EditForm()
    if form.validate_on_submit():
        new_rating = float(form.rating.data)
        new_review = form.review.data
        update_movie_by_id(movie_id, new_rating, new_review)
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    delete_movie_by_id(movie_id)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
