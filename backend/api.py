from flask.views import MethodView
from flask import request
from werkzeug.security import check_password_hash
import jwt
import datetime


class LoginAPI(MethodView):
    def post(self):
        # get the post data
        post_data = request.form
        try: 
            username = request.form["username"]
            password = request.form["password"]
        except KeyError:
            return {"error": "Må oppgi både brukernavn og passord"}, 401

        
        # Lage eget python dict for å slippe alt dette
        try:
            with open("../.venv/auth.txt", "r") as file:
                lines = [line.rstrip() for line in file.readlines()]
                admin = {"username": lines[0], "password": lines[1]}
        except FileNotFoundError:
            return {"error": "Feil med serveren, greier ikke finne admin bruker"}, 500


        if not username == admin["username"]:
            return {"error": "Feil brukernavn"}, 401

        elif not check_password_hash(admin["password"], password):
            return {"error": "Feil passord"}, 401

        token = jwt.encode({"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, "test")
        print(token)

        return {"token": token}
