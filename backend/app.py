from flask import Flask
from .api import LoginAPI
from .decorators import token_required

app = Flask(__name__)




@app.route("/")
def hello_world():
    return "Hello, World!"

# test url
@app.route("/p")
@token_required
def p():
    return {"m": "h"}

app.add_url_rule("/login/", view_func=LoginAPI.as_view("login"))