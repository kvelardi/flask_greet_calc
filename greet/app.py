# Make a simple Flask app that responds to these routes with simple text:
from flask import Flask

app= Flask(__name__)

# /welcome
# returns "welcome"
@app.route('/welcome')
def welcome():
    return "welcome"
  
# /welcome/home
# returns "welcome home"
@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

# /welcome/back
# returns "welcome back"
@app.route('/welcome/back')
def welcome_back():
    return "welcome back"