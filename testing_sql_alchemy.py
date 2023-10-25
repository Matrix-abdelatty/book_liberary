from flask import Flask
from flask_sqlalchemy import SQLAlchemy, session

app = Flask(__name__)

# CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = r"sqlite:///E:\All coursessssss\All  python staff\100 Days of Code\000-solutions and projects\Day 63 - Advanced - Databases and with SQLite and SQLAlchemy\library-start\sql_project\new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


def create_record(title, author, rating, id=None):
    if id is not None:
        new_book = Book(id=id, title=title, author=author, rating=rating)
        db.session.add(new_book)
    else:
        new_book =  Book(title=title, author=author, rating=rating)
        db.session.add(new_book)


# new_book = create_record(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.33333)


if __name__ == "__main__":
    with app.app_context():
        ## all operations must run in here
        db.create_all()
        test = create_record(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.33333)
        db.session.add(test)
        db.session.commit()

        app.run()
