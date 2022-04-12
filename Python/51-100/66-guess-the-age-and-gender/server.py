# Program to create a simple server using flask and jinja
# Guess the age and gender of name entered in the url
# Get blog data and show it in blog url+
# using jinja: it is a template engine
# predict the age of a name by using agify api: https://agify.io/
# determine the gender of a name using genderize api: https://genderize.io/

from flask import Flask, render_template
from datetime import date
import requests


app = Flask(__name__)


@app.route("/")
def home():
    """Dynamically render the current year."""

    current_year = date.today().year
    return render_template("index.html", year=current_year)


@app.route("/guess/<name>")
def guess(name):
    """Guesses the age and gender of the name in the url"""

    # getting the gender of the name
    genderize_response = requests.get(f"https://api.genderize.io?name={name}")
    genderize_response.raise_for_status()
    gender = genderize_response.json()["gender"]

    # getting the age of the name
    agify_response = requests.get(f"https://api.agify.io/?name={name}")
    agify_response.raise_for_status()
    age = agify_response.json()["age"]

    return render_template(
        "guess.html",
        person_name=name.capitalize(),
        person_gender=gender,
        person_age=age,
    )


@app.route("/blog")
def get_blog():
    """ Get all the blog posts from npoint bin"""
    blog_url = "https://api.npoint.io/b86d2da6502eab70217e"
    blog_response = requests.get(blog_url)
    blog_response.raise_for_status()

    all_posts = blog_response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
