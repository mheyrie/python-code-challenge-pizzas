from random import choice as rc, randint, choices, random

from faker import Faker

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

pizza_name = [
    "Chessy Chicken",
    "Chicken BBQ",
    "Margherita",
    "Mexican Beef",
    "Chesseburger",
    "Meaty BBQ",
    "Pepperoni",
    "Super Meaty",
    "Veggie Overlaod",
    "Spicy Mixed Pizza",
    "Shawarma",
    "Supreme",
    "Dodo Supreme",
    "Dodododod",
    "Fluffy Pizza",
    "Cooly"
]

pizza_ingredient = [
    "Cheese",
    "Plantain",
    "Beef",
    "Chili",
    "Suya",
    "Veggie",
    "Chicken",
    "Shawarma",
    "Tomatoes",
    "Red Pepper",
    "Broccoli",
    "Roasted Fennel",
    "Cauliflower",
    "Mushrooms",
    "Grilled Eggplant",
    "Grilled Pineapple",
    "Garlic",
    "Onions",
    "Jalapeños",
    "Capers",
    "Cashew Cream",
    "Balsamic Glaze"
]

with app.app_context():
    
    #Used to reset the db, deletes any previoue info on the db any time this file is initiated
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
 
  #Instantiating Restaurant
    restaurants = []
    for value in range(15):
        rt = Restaurant(
            name=fake.company(), 
            address=fake.address(),)
        restaurants.append(rt)

    db.session.add_all(restaurants)
    # print(restaurants)
    

    #Instantiating Pizza
    pizzas = []
    for value in range(15):
        
        pz = Pizza(
            name=pizza_name[value],
            ingredients=', '.join(choices(pizza_ingredient, k=3)),
            )
        pizzas.append(pz)

    db.session.add_all(pizzas)
  

    restaurant_pizzas = []
    for value in range(40):
        rp = RestaurantPizza(
            price = randint(1, 30)            
        ) 
        rp.pizza = rc(pizzas)
        rp.restaurant = rc(restaurants)

        restaurant_pizzas.append(rp)


    db.session.add_all(restaurant_pizzas)
    
    db.session.commit()


