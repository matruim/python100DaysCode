import datetime
import os
import urllib.parse
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Date, Float
from sqlalchemy.orm import Mapped, mapped_column
from wtforms import StringField, SubmitField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
import requests
from wtforms.widgets import NumberInput

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movie-list.db"
Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)


headers = {
            "Authorization": f"Bearer {os.getenv('TMDB_API_READ_ACCESS_TOKEN')}",
            'accept': 'application/json'
        }


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(4), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class EditMovieForm(FlaskForm):
    rating = DecimalField("Your Rating Out of 10", places=2,
              validators=[DataRequired(), NumberRange(0, 10, "Must be between 0-10")],
              widget=NumberInput(step=0.1))
    review = TextAreaField("Your Review", validators=[DataRequired()], render_kw={'rows': 3})
    submit = SubmitField('Update')


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField('Add Movie')


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies)-i

    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_movie(id):
    edit_form = EditMovieForm()
    movie = db.session.get(Movie, id)
    edit_form.rating.data = movie.rating
    edit_form.review.data = movie.review
    if request.method == 'POST':
        # do the updates that are needed
        movie.rating = request.form["rating"]
        movie.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=edit_form)


@app.route("/delete/<int:id>")
def delete_movie(id):
    movie = db.session.get(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    movie_form = AddMovieForm()
    if request.method == 'POST':
        movie_name = request.form['title']
        url = f"https://api.themoviedb.org/3/search/movie?query={urllib.parse.quote(movie_name)}"
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        raw_data = res.json()
        movie_data = raw_data['results']
        return render_template('select.html', options=movie_data)
    return render_template("add.html", form=movie_form)


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        res = requests.get(movie_api_url, headers=headers)
        data = res.json()
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'][:4],
            img_url=f"https://image.tmdb.org/t/p/original{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit_movie', id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)
