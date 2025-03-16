from flask import Blueprint, render_template,request,jsonify,redirect,url_for

home = Blueprint(__name__, "home")

@home.route("/home")
def home_page():
    return render_template("index.html")
@home.route("test")
def test():
    return render_template("profile.html")