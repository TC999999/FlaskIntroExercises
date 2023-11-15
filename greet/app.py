from flask import Flask, request

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    """Returns a welcome message"""
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    """Returns a welcome home message"""
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    """Returns a welcome back message"""
    return "welcome back"
