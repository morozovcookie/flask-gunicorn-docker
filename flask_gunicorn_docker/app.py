from flask_gunicorn_docker import __api_version__
from flask_gunicorn_docker.api import users_api_bp
from flask_gunicorn_docker.views import app


_url_prefix = '/api/{api_version}'.format(api_version=__api_version__)

app.register_blueprint(blueprint=users_api_bp, url_prefix='{url_prefix}/users'.format(url_prefix=_url_prefix))


if __name__ == '__main__':
    app.run()
