from flask import jsonify, request
from typing import Tuple

from flask_gunicorn_docker import storage
from flask_gunicorn_docker.api import users_api_bp
from flask_gunicorn_docker.repositories import UserRepository
from flask_gunicorn_docker.usecases import UsersList, StoreUser

user_repository = UserRepository(storage=storage)

user_list_use_case = UsersList(repository=user_repository)
store_user_use_case = StoreUser(repository=user_repository)


@users_api_bp.route(rule='/', methods=['GET'])
def get_users_list() -> Tuple[str, int]:
    try:
        result = user_list_use_case.do(
            limit=request.args.get('limit', 100),
            offset=request.args.get('offset', 0)
        )
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'message': e.__str__()}), 500


@users_api_bp.route(rule='/', methods=['POST'])
def store_user() -> Tuple[str, int]:
    try:
        store_user_use_case.do(user=None)
    except Exception as e:
        return jsonify({'message': e.__str__()}), 500

    return '', 201
