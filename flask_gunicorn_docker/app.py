from flask_gunicorn_docker import create_app, __api_version__
from flask_gunicorn_docker.api import users_api_bp


_url_prefix = '/api/{api_version}'.format(api_version=__api_version__)

app = create_app()
app.app_context().push()

app.register_blueprint(blueprint=users_api_bp, url_prefix='{url_prefix}/users'.format(url_prefix=_url_prefix))


if __name__ == '__main__':
    app.run()
