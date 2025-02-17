from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float

# db = sqlite3.connect('books.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE Book (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # cursor.execute("INSERT INTO Book VALUES(1, 'Harry Potter', 'J. K. Rowling', 9.3)")
# db.commit()

app = Flask(__name__)
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db=SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id:Mapped[int] =mapped_column(Integer,primary_key=True)
    title:Mapped[str] =mapped_column(String(250),unique=True,nullable=False)
    author:Mapped[str] =mapped_column(String(250),nullable=False)
    rating :Mapped[float]=mapped_column(Float,nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result=db.session.execute(db.select(Book).order_by(Book.title))
    all_book=result.scalars().all()
    return render_template('index.html',books=all_book)

@app.route('/rate')
def edit_rating():
    pass

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title= request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
