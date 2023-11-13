
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(50))

    # Establishes relationship between Restaurant model and the RestaurantPizza table
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.name} at {self.address}>'




# add any models you may need. 
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Establishes relationship between Pizza model and the RestaurantPizza table
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')

    def __repr__(self):
        return f'<Pizza {self.name}, Ingredients include: {self.ingredients}>'

 


class RestaurantPizza(db.Model, SerializerMixin):
     __tablename__ = 'restaurant_pizzas'

     id = db.Column(db.Integer, primary_key=True)
     price = db.Column(db.Integer)
     created_at = db.Column(db.DateTime, server_default=db.func.now())
     updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
     #Takes in Primary from both Restaurant and Pizza inform of a foreign key
     restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
     pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))


     def __repr__(self):
        return f'<RestaurantPizza {self.id} for {self.price}>'

    #Validation that price must be between 1 and 30
     @validates('price')
     def validate_price(self, key, price):
        if price < 1 or price >30:
            raise ValueError("Input Price between the range of 1 and 30")
        return price


