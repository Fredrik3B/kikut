from functools import wraps
from flask import request
import jwt

def token_required(f):
    # decorator funksjon som sjekker om token er gyldig for å gi tilgang til nettsiden
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("x-access-token")

        if not token:
            return {"error": "Mangler token"}, 401

        try:
            data = jwt.decode(token, "test", algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return {"error": "Token er for gammel"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Ikke gyldig token"}, 401
        
        return f(*args, **kwargs)

    return decorated  