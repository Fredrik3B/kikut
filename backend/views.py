from .api import LoginAPI
from .decorators import token_required
from flask import Blueprint

dashboard = Blueprint("dasboard", __name__)

@dashboard.route("/")
def hello_world():
    return "Hello, World!"

# test url
@dashboard.route("/p")
@token_required
def p():
    return {"m": "h"}

dashboard.add_url_rule("/login/", view_func=LoginAPI.as_view("login"))