from flask.views import MethodView
from flask import request
from werkzeug.security import check_password_hash

class LoginAPI(MethodView):
    """
    User Login Resource
    """
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
        print(username, admin["username"])


        if not username == admin["username"]:
            return {"error": "Feil brukernavn"}, 401

        elif not check_password_hash(admin["password"], password):
            return {"error": "Feil passord"}, 401

        return "Success"
        # if error is None:
        #     session.clear()
        #     session["user_id"] = user["id"]
        #     return redirect(url_for("index"))

        # try:
        #     # fetch the user data
        #     user = User.query.filter_by(
        #         email=post_data.get('email')
        #     ).first()
        #     if user and bcrypt.check_password_hash(
        #         user.password, post_data.get('password')
        #     ):
        #         auth_token = user.encode_auth_token(user.id)
        #         if auth_token:
        #             responseObject = {
        #                 'status': 'success',
        #                 'message': 'Successfully logged in.',
        #                 'auth_token': auth_token.decode()
        #             }
        #             return make_response(jsonify(responseObject)), 200
        #     else:
        #         responseObject = {
        #             'status': 'fail',
        #             'message': 'User does not exist.'
        #         }
        #         return make_response(jsonify(responseObject)), 404
        # except Exception as e:
        #     print(e)
        #     responseObject = {
        #         'status': 'fail',
        #         'message': 'Try again'
        #     }
        #     return make_response(jsonify(responseObject)), 500


