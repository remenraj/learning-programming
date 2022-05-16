# Top 10 Movies Website
# Movie details are obtained using The Movie Database API

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, os

# Movie DB details
MOVIE_DB_API_KEY = os.getenv("THE_MOVIE_DB_API_KEY")
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie/"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# Create the application instance
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6do3nzWlSihBXox7C0sKR6b"
Bootstrap(app)

# create movie database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Turn off deprecation warning
db = SQLAlchemy(app=app)


# create table
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


db.create_all()

# # Uncomment and run this code to add a movie into the database, if the database is empty
# # adding new movie to the database
# new_movie = Movies(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favorite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
#     )
# db.session.add(new_movie)
# db.session.commit()


class EditMovieForm(FlaskForm):
    """Form for editing movie details"""

    new_rating = StringField(
        "Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()]
    )
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddMovieForm(FlaskForm):
    """Form for adding new movie"""

    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # # getting all the movies data from the database
    # all_movies = db.session.query(Movies).all()

    # # getting all the movies data from the database and sorting them by ranking
    all_movies = Movies.query.order_by(Movies.rating).all()

    # all_movies = Movies.query.order_by(Movies.rating.desc()).all()    # order by descending

    # looping through all the movies
    for i in range(len(all_movies)):
        # giving each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edit movie details"""
    form = EditMovieForm()
    movie_id = request.args.get("id")
    movie = Movies.query.get(movie_id)

    if form.validate_on_submit():
        # Update the rating and review of the movie

        movie.rating = float(
            request.form["new_rating"]
        )  # movie.rating = form.new_rating.data
        movie.review = request.form["new_review"]  # movie.review = form.new_review.data

        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", form=form, movie=movie)


@app.route("/delete")
def delete_movie():
    """Delete a movie from the database"""
    movie_id = request.args.get("id")
    db.session.delete(Movies.query.get(movie_id))
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """Add a new movie to the database"""
    form = AddMovieForm()

    if form.validate_on_submit():
        lookup_movie_title = form.title.data

        movie_parameters = {
            "api_key": MOVIE_DB_API_KEY,
            "language": "en-US",
            "include_adult": "false",
            "query": lookup_movie_title,
        }

        movie_db_response = requests.get(
            url=MOVIE_DB_SEARCH_URL, params=movie_parameters
        )
        movie_db_response.raise_for_status()

        return render_template(
            "select.html", movies=movie_db_response.json()["results"]
        )

    return render_template("add.html", form=form)


@app.route("/select")
def select_movie():
    """Select a movie from the database"""
    # movie id
    movie_api_id = request.args.get("id")
    if movie_api_id:
        # get movie details from the API
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"

        movie_parameters = {
            "api_key": MOVIE_DB_API_KEY,
            "language": "en-US",
        }

        movie_db_response = requests.get(url=movie_api_url, params=movie_parameters)
        movie_db_response.raise_for_status()
        data = movie_db_response.json()

        new_movie = Movies(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"],
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit", id=new_movie.id))

    return render_template("select.html", movies=movie_db_response.json()["results"])


if __name__ == "__main__":
    app.run(debug=True)
