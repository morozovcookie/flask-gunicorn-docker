from os.path import join
from pathlib import Path
from flask import send_from_directory

from flask_gunicorn_docker import create_app


app = create_app()
app.app_context().push()

_assets_folder = join(Path(__file__).parent, '..', 'static', 'build')


@app.route(rule='/')
def index():
    # mode = environ.get('FLASK_ENV', 'production')
    # if mode == 'development':
    #     return ''

    return send_from_directory(
        directory=_assets_folder,
        filename='index.html'
    )



