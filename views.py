from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

class Products: 
    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image

headphones = Products('Headphones', 30, 'Pair of Samsung Wireless Headphones available for 30$', "static/headphones.jpg")
shoes = Products('Shoes', 40, 'The best Air Jordans availiable, the cheap price of 40$', "static/shoe.jpg")
earrings = Products('Earrings', 150, 'Louis earrings 24k gold and platinum plated, cost 150$', "static/earing.jpg")
product_list = [headphones, shoes, earrings]

@views.route('/')
def home():
    return render_template("home.html", products=product_list)

@views.route('/login')
def login():
    return render_template("login.html")