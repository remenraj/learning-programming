# SQLAlchemy
# SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create new database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False  # it will silence the deprecation warning in the console.
db = SQLAlchemy(app=app)


# create table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # __repr__ is a special method that is used to print the object.
    # this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return "<Title %r>" % self.title


# create the tables and database
db.create_all()


# adding new entry/CREATE RECORD
new_book = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)

# When creating new records, the primary key fields is optional, i.e,
# we can also write: new_book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3), the id field will be auto-generated.
db.session.add(new_book)
db.session.commit()


"""
Read All Records

    all_books = session.query(Book).all()


Read A Particular Record By Query

    book = Book.query.filter_by(title="Harry Potter").first()


Update A Particular Record By Query

    book_to_update = Book.query.filter_by(title="Harry Potter").first()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()  


Update A Record By PRIMARY KEY

    book_id = 1
    book_to_update = Book.query.get(book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()  


Delete A Particular Record By PRIMARY KEY

    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

You can also delete by querying for a particular value e.g. by title or one of the other properties.
"""
