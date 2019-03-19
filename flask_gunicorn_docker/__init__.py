from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_gunicorn_docker.api import url_prefix, users_api_bp


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=users_api_bp, url_prefix='{url_prefix}/users'.format(url_prefix=url_prefix))

    # db.init_app(app=app)
    flask_bcrypt.init_app(app=app)

    return app
