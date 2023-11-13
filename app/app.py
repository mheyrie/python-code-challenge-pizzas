#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Restaurant, Pizza, RestaurantPizza


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home_testing():
    return '<h1>This is just for testing remember to delete</h1>'

@app.route('/restaurants', methods=['GET'])
def restaurants():
    if request.method == 'GET':
        restaurants = Restaurant.query.all()

        response = make_response(
            jsonify([restaurant.to_dict() for restaurant in restaurants]),
            200
        )

        return response

    
    
@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id==id).all(RestaurantPizza.pizza_id)
    if request.method == 'GET':
        
        response = make_response(jsonify(restaurant.to_dict()), 200)
        return response
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
