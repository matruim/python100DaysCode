from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float, delete
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


# with app.app_context():
# new_book = Book(title="The Blue Sword", author="Robin McKinley", rating=9.2)
# db.session.add(new_book)
# db.session.commit()
# result = db.session.execute(db.select(Book).order_by(Book.title))
# all_books = result.scalars()
# print(all_books)
#
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     print(book)
#
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
# with app.app_context():
#     # book_to_update = db.session.execute(db.select(Book).where(Book.id == 2)).scalar()
#     book_to_update = db.get_or_404(Book, 2)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()
#
# with app.app_context():
#     # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     book_to_delete = db.get_or_404(Book, 2)
#     db.session.delete(book_to_delete)
#     db.session.commit()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit_book(id):
    book = db.session.get(Book, id)
    if request.method == 'POST':
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)

@app.route('/delete/<int:id>')
def delete_book(id):
    book = db.session.get(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=9000)
