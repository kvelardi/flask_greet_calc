# Build a simple calculator with Flask

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)
# -uses URL query parameters to get the numbers to calculate
# -responds to 4 different routes
# -each route does a different math operation with two numbers 

    # /add
@app.route('/add')
def add_nums():
    a = int(request.args.get ('a'))
    b = int(request.args.get ('b'))
    result = add(a, b)

    return str (result)

    # /sub
@app.route('/sub')
def sub_nums():
    a = int(request.args.get ('a'))
    b = int(request.args.get ('b'))
    result = sub(a, b)

    return str (result)
    # /mult
@app.route('/mult')
def mult_nums():
    a = int(request.args.get ('a'))
    b = int(request.args.get ('b'))
    result = mult(a, b)

    return str (result)

    # /div
@app.route('/div')
def div_nums():
    a = int(request.args.get ('a'))
    b = int(request.args.get ('b'))
    result = div(a, b)

    return str (result)



# -responds to a fifth route that does a math operation with two numbers
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operator>')
def math(operator):
    a = int(request.args.get ('a'))
    b = int(request.args.get ('b'))
    result = operators[operator](a, b)

    return str (result)