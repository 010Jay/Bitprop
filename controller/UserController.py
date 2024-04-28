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


@user_api.route('/user/read/<user_id>', methods=['GET'])
def get_user(user_id):
    user = db.read(user_id)
    return jsonify({'user': user})


@user_api.route('/user/create', methods=['POST'])
def create_user():
    data = json.dumps(request.json)
    user = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    db.create(user)
    return jsonify({'user': request.json})


@user_api.route('/user/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.delete(user_id)
    message = "User has been deleted."
    return jsonify({'Message': message})
