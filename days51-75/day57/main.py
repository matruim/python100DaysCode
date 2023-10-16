import datetime
import random
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.date.today().strftime("%Y")
    my_name = "Jared Good"
    return render_template('index.html', num=random_number, year=year, name=my_name)


@app.route('/guess/<name>')
def guess(name):
    res = requests.get(f"https://api.genderize.io/?name={name}")
    res.raise_for_status()
    gender = res.json()["gender"]
    res = requests.get(f"https://api.agify.io/?name={name}")
    res.raise_for_status()
    age = res.json()["age"]
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    res = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
    posts = res.json()
    print(posts)
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
