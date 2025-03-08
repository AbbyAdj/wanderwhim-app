from flask import Blueprint, render_template



all_routes = Blueprint("routes", __name__)

@all_routes.route("/home")
def homepage():
    return render_template("homepage.html")

@all_routes.route("/login")
def login():
    return render_template("login.html")

@all_routes.route("/travel/form")
def input_form():
    return render_template("input_form.html")

@all_routes.route("/account/<user>")
def user_info():
    return render_template("user_info.html")

@all_routes.route("/city/<city: str>")
def city_information(city):
    return render_template("city_information.html", city=city)

all_routes.route("/travel/results")
def travel_result():
    # This is the same as the dice result (I mean the template). Keep the dice html but use this for both. If you find that
    # this template is a bit cumbersome, switch to use dice for its designated purpose.
    return render_template("spontaneous_result.html")

all_routes.route("/travel/dice_roll")
def dice_result():
    return render_template("dice.html")





