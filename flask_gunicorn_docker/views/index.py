from os.path import join, exists
from pathlib import Path
from flask import send_from_directory

from flask_gunicorn_docker import create_app


app = create_app()
app.app_context().push()

_build_folder = join(Path(__file__).parent, '..', 'static', 'build')
_assets_folder = join(_build_folder, 'static')


@app.route('/', defaults={'filename': ''})
@app.route('/<path:filename>')
def index(filename):
    if filename != '':
        if exists(join(_build_folder, filename)):
            return send_from_directory(directory=_build_folder, filename=filename)

        if exists(join(_assets_folder, filename)):
            return send_from_directory(directory=_assets_folder, filename=filename)

    return send_from_directory(directory=_build_folder, filename='index.html')


@app.route('/static/<path:filename>')
def static(filename):
    return send_from_directory(directory=_assets_folder, filename=filename)
