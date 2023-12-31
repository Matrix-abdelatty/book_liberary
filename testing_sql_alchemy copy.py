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


# CREATE RECORD
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)


# Create A New Record
new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
# note: When creating new records, the primary key fields is optional. you can also write:
# new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# the id field will be auto-generated.

############
############
############

# Read All Records
all_books = session.query(Book).all()


# Read A Particular Record By Query
book = Book.query.filter_by(title="Harry Potter").first()


# Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()


# Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()


# Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
# You can also delete by querying for a particular value e.g. by title or one of the other properties.


if __name__ == "__main__":
    with app.app_context():
        # all operations must run in here
        db.create_all()
        db.session.add(new_book)
        db.session.commit()

        app.run()
