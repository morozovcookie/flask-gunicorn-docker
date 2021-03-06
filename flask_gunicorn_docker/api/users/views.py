from logging import getLogger
from flask import jsonify, request
from typing import Tuple

from .blueprint import users_api_bp
from flask_gunicorn_docker import storage, FlaskUnicornDockerBaseException
from flask_gunicorn_docker.repositories import UserRepository
from flask_gunicorn_docker.usecases import UsersList, StoreUser

user_repository = UserRepository(storage=storage)

user_list_use_case = UsersList(repository=user_repository)
store_user_use_case = StoreUser(repository=user_repository)

gunicorn_logger = getLogger('gunicorn.error')


@users_api_bp.route(rule='/', methods=['GET'])
def get_users_list() -> Tuple[str, int, dict]:
    try:
        result = user_list_use_case.do(
            limit=request.args.get('limit', 100),
            offset=request.args.get('offset', 0)
        )
        return jsonify(result), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({'message': e.__str__()}), 500, {'Content-Type': 'application/json'}


@users_api_bp.route(rule='/', methods=['POST'])
def store_user() -> Tuple[str, int, dict]:
    try:
        store_user_use_case.do(user=request.json)
    except FlaskUnicornDockerBaseException as e:
        return jsonify({'message': e.__str__()}), 400, {'Content-Type': 'application/json'}
    except Exception as e:
        gunicorn_logger.error(e.__str__())
        return '', 500, {'Content-Type': 'application/json'}

    return '', 201, {'Content-Type': 'application/json'}
