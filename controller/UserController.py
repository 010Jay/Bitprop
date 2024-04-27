import json

from types import SimpleNamespace

from repository.UserRepository import UserRepository

from flask import jsonify, request, Blueprint


user_api = Blueprint('user_api', __name__)
db = UserRepository()


@user_api.route('/user/readAll', methods=['GET'])
def get_users():
    user_list = db.read_all()
    return jsonify({'users': user_list})


@user_api.route('/user/create', methods=['POST'])
def create_user():
    data = json.dumps(request.json)
    user = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    db.create(user)
    return data


@user_api.route('/user/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.delete(user_id)
    return "User has been deleted."
