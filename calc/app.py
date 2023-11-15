# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_numbers():
    num_a = int(request.args["a"])
    num_b = int(request.args["b"])
    sum = add(num_a, num_b)
    return str(sum)


@app.route("/sub")
def subtract_numbers():
    num_a = int(request.args["a"])
    num_b = int(request.args["b"])
    diff = sub(num_a, num_b)
    return str(diff)


@app.route("/mult")
def multiply_numbers():
    num_a = int(request.args["a"])
    num_b = int(request.args["b"])
    prod = mult(num_a, num_b)
    return str(prod)


@app.route("/div")
def divide_numbers():
    num_a = int(request.args["a"])
    num_b = int(request.args["b"])
    quot = div(num_a, num_b)
    return str(quot)


@app.route("/math/<calc>")
def calc_numbers(calc):
    num_a = int(request.args["a"])
    num_b = int(request.args["b"])
    operations = {
        "add": add(num_a, num_b),
        "sub": sub(num_a, num_b),
        "mult": mult(num_a, num_b),
        "div": div(num_a, num_b),
    }
    return str(operations[calc])
