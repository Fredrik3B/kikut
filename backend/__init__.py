from flask import Flask
from .views import dashboard


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(dashboard)

    return app