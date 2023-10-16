from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

res = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
posts = res.json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    post = next(p for p in post_objects if p.id == index)
    return render_template("single-post.html", post=post, posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", posts=posts)

@app.route('/contact')
def contact():
    return render_template("contact.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
