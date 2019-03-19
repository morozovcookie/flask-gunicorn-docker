from flask import Blueprint, jsonify

users_api_bp = Blueprint(name='user_api', import_name=__name__)


@users_api_bp.route(rule='/', methods=['GET'])
def get_users_list():
    return jsonify([])


@users_api_bp.route(rule='/', methods=['POST'])
def store_user():
    return '', 201
