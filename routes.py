from flask import Blueprint, render_template

# check https://startbootstrap.com/templates/general?showPro=false

all_routes = Blueprint("routes", __name__)

@all_routes.route("/login")
def login():
    return render_template("login.html")

@all_routes.route("/account/<user>")
def user_info():
    return render_template("user_info.html")

@all_routes.route("/home")
def homepage():
    return render_template("homepage.html")

all_routes.route("/city/<city: str>")
def city_information(city):
    return render_template("city_information.html", city=city)

all_routes.route("/travel/form")
def input_form():
    return render_template("input_form.html")

all_routes.route("/travel/dice_roll")
def dice_result():
    return render_template("dice.html")

all_routes.route("/travel/results")
def travel_result():
    return render_template("spontaneous_result.html")



