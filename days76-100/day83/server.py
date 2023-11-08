from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NEEDTOMAKEASECRETKEY12345'
Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


if __name__ == "__main__":
    app.run(debug=True, port=9000)