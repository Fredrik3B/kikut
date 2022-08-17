from werkzeug.security import check_password_hash
from flask import current_app

def validate_login(username, password):
    
    try:
        admin = current_app.config["ADMIN"]
    except KeyError:
        return {"error": "Feil med serveren, greier ikke finne admin bruker"}, 500


    if not username == admin["username"]:
        return "Feil brukernavn"

    elif not check_password_hash(admin["password"], password):
        return "Feil passord"

    return True