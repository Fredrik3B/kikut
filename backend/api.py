from flask.views import MethodView
from flask import request, current_app
import jwt
import datetime
from .auth import validate_login


class LoginAPI(MethodView):
    def post(self):
        # Få innloggingsdataen fra brukeren
        post_data = request.form
        try: 
            username = request.form["username"]
            password = request.form["password"]
        except KeyError:
            return {"error": "Må oppgi både brukernavn og passord"}, 401

        # sjekker om brukernavn og passord stemmer, hvis ikke gi tilbakemeldig på hva som er galt
        login_status = validate_login(username, password)
        if login_status is not True:
            return {"error": login_status}, 401

        # lager en json web token som er gyldig i 6 timer, denne brukes i x-access-token headeren for å få tilgang til nettsiden
        token = jwt.encode({"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, current_app.config["SECRET_KEY"])

        return {"token": token}
