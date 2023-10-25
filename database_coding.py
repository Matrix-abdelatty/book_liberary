from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)


current_dir = os.path.dirname(os.path.abspath(__file__)) # Use the os module to get the current directory of  Python script
db_path = os.path.join(current_dir, 'new-books-collection.db') # path to your database file relative to the current directory
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username_string = db.Column(db.String(250), unique=True, nullable=False)
    email_string = db.Column(db.String(250), unique=True, nullable=False)
    password_string = db.Column(db.String(250),  nullable=False)

