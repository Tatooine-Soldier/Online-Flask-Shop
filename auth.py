from cgitb import text
from multiprocessing.spawn import import_main_path
from flask import Blueprint, render_template, redirect, url_for, request, session 
import sqlite3
import random

def create_num():
    num = random.randint(1000, 100000)
    return num

connect = sqlite3.connect('my.db', check_same_thread=False)
cur = connect.cursor()
# cur.execute("SELECT * FROM Users")
# result = cur.fetchall()
# for row in result:
#     print(row)

auth = Blueprint('auth', __name__)

name = ""


class User():
    def __init__(self, username, password, logged_in):
        self.username = username
        self.password = password
        self.logged_in = logged_in


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("auth.user", usr=user, cart=0))
    else:
        return render_template("login.html")

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    try:
        if request.method == "POST":
            user = request.form["name"]
            password = request.form['password']
            insert_statement = """INSERT INTO Users (user_id, username, password) 
                                  VALUES (?, ?, ?);"""
            important_data = (create_num(), user, password)
            cur.execute(insert_statement, important_data)
            cur.execute('SELECT * FROM Users')
            outcome = cur.fetchall()
            for i in outcome:
                print(i)
            #new_user = User(user, password, True)
            return redirect(url_for("auth.user", usr=user, cart=0))
    except Exception as e:
        print(e)
    connect.commit()
    return render_template("signup.html")

@auth.route("/#<usr>/<cart>", methods=["GET","POST"])
def user(usr, cart):
    return render_template("user_profile.html", text=usr, track=cart)

@auth.route("/<titl>/<price>/<desc>", methods=["GET","POST"])
def product(price, titl, desc):
    return render_template("product.html", obj=price, text=titl, odesc=desc)


# data = request.form
        # name = data['name']
        # password = data['password']
