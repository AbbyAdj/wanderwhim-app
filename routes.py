from flask import Blueprint, render_template

all_routes = Blueprint("routes", __name__)

@all_routes.route("/")
def homepage():
    return render_template("/templates/homepage.html")

