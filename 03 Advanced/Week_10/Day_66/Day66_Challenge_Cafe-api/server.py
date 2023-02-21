from random import choice

from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# this can also be done in one go in the post_add()
def add_cafe(name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
    new_cafe = Cafe(
        name=name,
        map_url=map_url,
        img_url=img_url,
        location=location,
        seats=seats,
        has_toilet=has_toilet,
        has_wifi=has_wifi,
        has_sockets=has_sockets,
        can_take_calls=can_take_calls,
        coffee_price=coffee_price
    )
    db.session.add(new_cafe)
    db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/all')
def get_all():
    with app.app_context():
        cafes = db.session.query(Cafe).all()
    all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=all_cafes)


@app.route('/random')
def get_random():
    with app.app_context():
        cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/search', methods=['GET', 'POST'])
def get_search():
    loc = request.args.get('loc')
    with app.app_context():
        cafe = db.session.query(Cafe).filter_by(location=loc).first()
        if cafe:
            return jsonify(cafe=cafe.to_dict())
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
@app.route('/add', methods=['GET', 'POST'])
def post_add():
    name = request.args.get('name')  # "Science Gallery London"
    map_url = "https://g.page/scigallerylon?share"  # request.args.get('map_url')
    img_url = "https://atlondonbridge.com/wp-content/uploads/2019/02/Pano_9758_9761-Edit-190918_LTS_Science_Gallery" \
              "-Medium-Crop-V2.jpg "  # request.args.get('img_url')
    location = "London Bridge"  # request.args.get('loc')
    seats = "50+"  # request.args.get('seats')
    has_toilet = True  # request.args.get('has_toilet')
    has_wifi = True  # request.args.get('has_wifi')
    has_sockets = True  # request.args.get('has_sockets')
    can_take_calls = True  # request.args.get('can_take_calls')
    coffee_price = "\u00a32.40"  # request.args.get('coffee_price')
    add_cafe(name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price)

    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update_price/<int:cafe_id>', methods=['GET', 'POST'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")   # \u00a32.60
    with app.app_context():
        cafe = db.session.query(Cafe).get(cafe_id)
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
