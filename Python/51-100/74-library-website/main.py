# Library website
# View, add, edit, and delete books
# Flask URL building: https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building

from flask import (
    Flask,
    render_template,
    render_template_string,
    request,
    redirect,
    url_for,
)
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
Bootstrap(app=app)
# create new database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False  # it will silence the deprecation warning in the console.
db = SQLAlchemy(app=app)


# create Books table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


# create the tables and database
db.create_all()


@app.route("/")
def home():
    """Home page"""
    # read all records
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Add new book"""
    if request.method == "POST":
        data = request.form

        new_book = Books(
            title=data["title"], author=data["author"], rating=data["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edit book"""
    if request.method == "POST":
        # Update the rating of the book
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))

    book_id = request.args.get("id")
    book_selected = Books.query.get(book_id)

    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    """Delete a book from the database"""
    book_id = request.args.get("id")
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
