from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_bcrypt import Bcrypt
from os import environ

from flask_gunicorn_docker.infrastructure import PostgresService
from flask_gunicorn_docker.version import __version__, __api_version__


master_engine = create_engine('postgres://{username}:{password}@{host}:{port}/{database}'.format(
    username=environ['POSTGRESQL_MASTER_USERNAME'],
    password=environ['POSTGRESQL_MASTER_PASSWORD'],
    host=environ['POSTGRESQL_MASTER_HOST'],
    port=environ['POSTGRESQL_MASTER_PORT'],
    database=environ['POSTGRESQL_MASTER_DATABASE']
))
master_session = sessionmaker(bind=master_engine, autoflush=True, autocommit=True, expire_on_commit=True)

slave_engine = create_engine('postgres://{username}:{password}@{host}:{port}/{database}'.format(
    username=environ['POSTGRESQL_SLAVE_USERNAME'],
    password=environ['POSTGRESQL_SLAVE_PASSWORD'],
    host=environ['POSTGRESQL_SLAVE_HOST'],
    port=environ['POSTGRESQL_SLAVE_PORT'],
    database=environ['POSTGRESQL_SLAVE_DATABASE']
))
slave_session = sessionmaker(bind=slave_engine, autoflush=True, autocommit=True, expire_on_commit=True)

storage = PostgresService(master=master_session, slave=slave_session)

Base = declarative_base()
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    flask_bcrypt.init_app(app=app)

    return app
