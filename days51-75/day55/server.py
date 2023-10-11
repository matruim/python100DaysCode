import random

from flask import Flask

app = Flask(__name__)

print(__name__)

random_num = random.randint(0, 9)

@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTBsdG1xOTZ2eGExOXZ0bjk5bWZ2ZDVtZjBtMDNhd2Fia2FzZnk1cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DhiRqIsofVMi7fWNBQ/giphy.gif" />'


@app.route('/<int:guess>')
def guessing_game(guess):
    global random_num
    if guess > random_num:
        return ('<h2>To High. Try a lower number</h2>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif guess < random_num:
        return ('<h2>To Low. Try a higher number</h2>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        random_num = random.randint(0, 9)
        return ('<h2>You Got it!</h2>'
                '<p>The number has been changed try to guess the new number.</p>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
