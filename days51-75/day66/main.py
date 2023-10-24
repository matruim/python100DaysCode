import random
from dataclasses import dataclass
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
@dataclass
class Cafe(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(250), unique=True, nullable=False)
    map_url: str = db.Column(db.String(500), nullable=False)
    img_url: str = db.Column(db.String(500), nullable=False)
    location: str = db.Column(db.String(250), nullable=False)
    seats: str = db.Column(db.String(250), nullable=False)
    has_toilet: bool = db.Column(db.Boolean, nullable=False)
    has_wifi: bool = db.Column(db.Boolean, nullable=False)
    has_sockets: bool = db.Column(db.Boolean, nullable=False)
    can_take_calls: bool = db.Column(db.Boolean, nullable=False)
    coffee_price: str = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """
        Render the homepage.

        Returns:
            HTML: The homepage.
        """
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    """
        Get a random cafe from the database.

        Returns:
            JSON: A randomly selected cafe.
        """
    return jsonify(random.choice(Cafe.query.all()))


@app.route("/all")
def all_cafes():
    """
        Get a list of all cafes in the database.

        Returns:
            JSON: A list of all cafes.
        """
    return jsonify(Cafe.query.all())


@app.route("/search")
def find_cafe():
    """
        Find cafes by location.

        Parameters:
            loc (str): The location to search for.

        Returns:
            JSON: A list of cafes matching the location.
        """
    location = request.args.get('loc')
    cafes = Cafe.query.filter_by(location=location).all()
    if len(cafes) == 0:
        return error('location')
    return jsonify(cafes)


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    """
        Create a new Cafe.

        Parameters:
            name (str): Name of the cafe.
            map_url (str): google map link to cafe location
            img_url (str): link to image of cafe
            loc (str): The city of the cafe
            sockets (bool): if the cafe has power plugs available
            toilet (bool): if the cafe has a restroom open to public
            wifi (bool): if cafe has wifi access for public
            seats (str): number of seats at cafe
            coffee_price(str): Cost of a cup of coffee

        Returns:
            JSON: a success message if everything went well.
    """
    cafe_data = {key: request.form.get(key) for key in [
        "name", "map_url", "img_url", "loc", "sockets", "toilet", "wifi", "calls", "seats", "coffee_price"
    ]}
    new_cafe = Cafe(**cafe_data)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH, PUT"])
def update_price(cafe_id):
    """
        Update the price of a coffee at the Cafe

        Parameters:
            cafe_id (int): Cafe id number

        Returns:
            JSON: message of success or error
    """
    cafe = Cafe(id=cafe_id)
    if cafe.name is None:
        return error('id')

    cafe.coffee_price = request.args.get('new_price')
    db.session.commit()


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    """
            Delete a Cafe

            Parameters:
                cafe_id (int): Cafe id number

            Returns:
                JSON: message of success or error
        """
    cafe = Cafe(id=cafe_id)
    if cafe.name is None:
        return error('id')

    db.session.delete(cafe)
    db.session.commit()


def error(error_type):
    if error_type == "location":
        return {
            'error': {
                "Not Found": "Sorry, we dont have a cafe at that location."
            }
        }, 404
    if error_type == "id":
        return {
            'error': {
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        }, 404


if __name__ == '__main__':
    app.run(debug=True, port=8080)
