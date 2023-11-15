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
            jsonify([restaurant.to_dict(rules=('-pizzas',)) for restaurant in restaurants]),
            200
        )

        return response

    
    
@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id==id).first()
    if restaurant == None:
        response_body = {
            "error": "Restaurant not found"
        }
        repsonse = make_response(response_body, 404)
        return repsonse
    else:
        if request.method == 'GET':
            return make_response(jsonify(restaurant.to_dict()), 200)
        
        elif request.method == 'DELETE':
                db.session.delete(restaurant)
                db.session.commit()

                response_body = {
                    
                }
                repsonse = make_response(
                    response_body, 
                    200
                )
                return repsonse


@app.route('/pizzas', methods=['GET'])
def pizzas():
    if request.method == 'GET':
        pizzas = Pizza.query.all()

        response = make_response(
            jsonify([pizza.to_dict() for pizza in pizzas]),
            200
        )

        return response 
    


@app.route('/restaurant_pizzas', methods=['GET', 'POST'])
def restaurant_pizzas():

    if request.method == 'GET':
        restaurant_pizzas = []
        for restaurant_pizza in RestaurantPizza.query.all():
            restaurant_pizza_dict = restaurant_pizza.to_dict()
            restaurant_pizzas.append(restaurant_pizza_dict)

        response = make_response(
            jsonify(restaurant_pizzas),
            200
        )

    else:
        if request.method == 'POST':
            new_restaurant_pizza = RestaurantPizza(
                price = request.form.get("price"),
                pizza_id = request.form.get("pizza_id"),
                restaurant_id = request.form.get("restaurant_id"),
            )

            db.session.add(new_restaurant_pizza)
            db.session.commit()

            restaurant_pizza_dict = new_restaurant_pizza()

            response = make_response(
                restaurant_pizza_dict,
                201
            )

            return response
        else:
            if new_restaurant_pizza == None:
                response_body = {
                            "errors": ["validation errors"]
                            }
                repsonse = make_response(response_body, 404)
        return repsonse
    
        


    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
