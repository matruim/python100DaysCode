from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"""<b>{function()}</b>"""

    return wrapper


def make_italics(function):
    def wrapper():
        return f"""<em>{function()}</em>"""

    return wrapper


def make_underline(function):
    def wrapper():
        return f"""<u>{function()}</u>"""

    return wrapper


@app.route("/")
def hello_world():
    return '<h1>Hello, World</h1>'


@app.route("/bye")
@make_bold
@make_italics
@make_underline
def bye():
    return "Bye!"


@app.route("/<name>")
def greet(name):
    return f"Hello, {name}!"


@app.route("/<name>/<int:age>")
def greet2(name, age):
    return f"Hello, {name}, you are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)
