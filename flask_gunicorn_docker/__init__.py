from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    db.init_app(app=app)
    flask_bcrypt.init_app(app=app)

    return app
