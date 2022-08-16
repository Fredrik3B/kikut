from flask import Flask
from .api import LoginAPI

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

app.add_url_rule("/login/", view_func=LoginAPI.as_view("login"))
# @app.route("/login/", methods=("GET", "POST"))
# def login():
#     if request.method == "POST":
#         print(request.get_json())
