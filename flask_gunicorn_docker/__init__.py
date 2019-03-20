from os import environ
from os.path import join
from pathlib import Path
from logging import getLogger
from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

_assets_folder = join(Path(__file__).parent, 'static', 'build', 'static')


def create_app():
    app = Flask(import_name=__name__, static_folder=_assets_folder)

    gunicorn_logger = getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    flask_bcrypt.init_app(app=app)

    return app
