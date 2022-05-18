# Cafe API
# Using postman to test the API
# URL for API documentation on Postman: https://documenter.getpostman.com/view/20674071/UyrDDFLo

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# cafe table
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
    
    def to_dict(self, all=None):
        """Converts the object to a dictionary"""
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        # if all is not None:
        #     for _ in range(len())
        # else:
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
            
        return dictionary
        
        # #Method 2. Alternatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        
        # to avoid id column
        # return {column.name:getattr(self, column.name) for column in self.__table__.columns if column.name != 'id'}


@app.route("/")
def home():
    """Home page"""
    return render_template("index.html")


@app.route(
    "/random"
)  # GET method(methods=["GET"]) is allowed by default on all routes.
def get_random_cafe():
    """Returns a random cafe"""
    # # Apparently this is the quickest way to get a random row from a database that may become large / Scalability
    # # Firstly, get the total number of rows in the database
    # row_count = Cafe.query.count()
    # # Generate a random number for skipping some records
    # random_offset = random.randint(0, row_count-1)
    # # Return the first record after skipping random_offset rows
    # random_cafe = Cafe.query.offset(random_offset).first()

    # Cafe.query == db.session.query(Cafe)
    random_cafe = random.choice(Cafe.query.order_by(Cafe.id).all())
    # print(random_cafe)    # prints: <cafe 13>

    # return jsonify(
    #     cafe={
    #         # Omit the id from the response
    #         # "id": random_cafe.id,
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
            
    #         # Put some properties in a sub-category
    #         "amenities": {
    #             "seats": random_cafe.seats,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "has_sockets": random_cafe.has_sockets,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "coffee_price": random_cafe.coffee_price,
    #         },
    #     }
    # )
    
    return jsonify(cafe=random_cafe.to_dict())

    
@app.route("/all")
def all():
    """Returns all cafes"""

    all_cafe = Cafe.query.all()
    # print(all_cafe)   # prints list of: [<cafe 1>, <cafe 2>, <cafe 3>, <cafe 4>, <cafe 5>, <cafe 6>]
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafe])


@app.route("/search")
def search():
    """Returns all cafes matching the search term"""
    query_location = request.args.get("loc")

    result = Cafe.query.filter_by(location=query_location).all()

    if result:
        return jsonify(cafe=[cafe.to_dict() for cafe in result])
    else:
        return jsonify(error={"Not found":"Sorry, we don't have a cafe at that location"})
    

@app.route("/add", methods=["POST"])
def add_cafe():
    """Adds a new cafe"""
    # Get the data from the request
    cafe_name = request.form.get("name")
    cafe_map_url = request.form.get("map_url")
    cafe_img_url = request.form.get("img_url")
    cafe_location = request.form.get("location")
    cafe_seats = request.form.get("seats")
    cafe_has_toilet = bool(request.form.get("has_toilet"))  # or request.form.get('has_toilet', type=bool)
    cafe_has_wifi = bool(request.form.get("has_wifi"))
    cafe_has_sockets = bool(request.form.get("has_sockets"))
    cafe_can_take_calls = bool(request.form.get("can_take_calls"))
    cafe_coffee_price = request.form.get("coffee_price")
    
    # The bool() function returns the boolean value of a specified object.
    # The object will always return True, unless:
    # The object is empty, like [], (), {}
    # The object is False
    # The object is 0
    # The object is None

    # Create a new cafe object
    new_cafe = Cafe(
        name=cafe_name,
        map_url=cafe_map_url,
        img_url=cafe_img_url,
        location=cafe_location,
        seats=cafe_seats,
        has_toilet=cafe_has_toilet,
        has_wifi=cafe_has_wifi,
        has_sockets=cafe_has_sockets,
        can_take_calls=cafe_can_take_calls,
        coffee_price=cafe_coffee_price,
    )

    # Add the new cafe to the database
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    """Updates the price of the coffee"""
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price  = request.args.get("price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    
    else:
        return jsonify(error={"Not found":"Sorry, cafe with that id is not found in the database."})


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def cafe_closed(cafe_id):
    api_key = "SecretAPIKey"
    api_key_entered = request.args.get("api_key")

    if api_key == api_key_entered:
        try:
            db.session.delete(Cafe.query.get(cafe_id))
        except:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else:
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == "__main__":
    app.run(debug=True)
