import json

from types import SimpleNamespace

from repository.OrderRepository import OrderRepository

from flask import jsonify, request, Blueprint

order_api = Blueprint('order_api', __name__)
db = OrderRepository()


@order_api.route('/order/readAll', methods=['GET'])
def get_orders():
    order_list = db.read_all()
    return jsonify({'orders': order_list})


@order_api.route('/order/read/<order_id>', methods=['GET'])
def get_order(order_id):
    order = db.read(order_id)
    return jsonify({'order': order})


@order_api.route('/order/create', methods=['POST'])
def create_order():
    data = json.dumps(request.json)
    order = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    db.create(order)
    return jsonify({'order': request.json})


@order_api.route('/order/delete/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    db.delete(order_id)
    message = "User has been deleted."
    return jsonify({'Message': message})

