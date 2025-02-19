from flask import Flask
from sqlalchemy import String, Integer, Float
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-book-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# create table
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# # crate record
# with app.app_context():
#     new_book = Books(id=3, title="array Potter", author=" K.J. Rowling", rating=9)
#     db.session.add(new_book)
#     db.session.commit()

#all record show
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

#particular record show
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "harry Potter")).scalar()


#update
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

#update buy id
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()

# delete by id
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()

with app.app_context():
    all_books = Books.query.all()
    for book in all_books:
        print(book.id, book.title)