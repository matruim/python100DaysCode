import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dataclasses import dataclass

ckeditor = CKEditor()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
@dataclass
class BlogPost(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(250), unique=True, nullable=False)
    subtitle: str = db.Column(db.String(250), nullable=False)
    date: str = db.Column(db.String(250), nullable=False)
    body: str = db.Column(db.Text, nullable=False)
    author: str = db.Column(db.String(250), nullable=False)
    img_url: str = db.Column(db.String(250), nullable=False)


class CreatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired(), URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    data = BlogPost.query.all()
    posts = []
    posts = data if data is not None else []
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    new_form = CreatePostForm()
    if request.method == 'POST':
        post = BlogPost(
            title=request.form["title"],
            subtitle=request.form["subtitle"],
            date=date.today().strftime('%B %d, %Y'),
            body=request.form["body"],
            author=request.form["author"],
            img_url=request.form["img_url"],
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=new_form)


@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    edit_form = CreatePostForm(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        author=requested_post.author,
        img_url=requested_post.img_url,
        body=requested_post.body
    )

    if request.method == 'POST':
        requested_post.title = request.form['title']
        requested_post.subtitle = request.form['subtitle']
        requested_post.author = request.form['author']
        requested_post.img_url = request.form['img_url']
        requested_post.body = request.form['body']
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template("make-post.html", post=requested_post, form=edit_form)


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    db.session.delete(BlogPost.query.get_or_404(post_id))
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
