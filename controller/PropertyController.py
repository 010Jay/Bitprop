import json

from types import SimpleNamespace

from repository.PropertyRepository import PropertyRepository

from flask import jsonify, request, Blueprint

property_api = Blueprint('property_api', __name__)
db = PropertyRepository()


@property_api.route('/property/readAll', methods=['GET'])
def get_properties():
    property_list = db.read_all()
    return jsonify({'property': property_list})


@property_api.route('/property/read/<property_id>', methods=['GET'])
def get_property(property_id):
    prop = db.read(property_id)
    return jsonify({'property': prop})


@property_api.route('/property/create', methods=['POST'])
def create_property():
    data = json.dumps(request.json)
    prop = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    db.create(prop)
    return jsonify({'property': request.json})


@property_api.route('/property/delete/<property_id>', methods=['DELETE'])
def delete_property(property_id):
    db.delete(property_id)
    message = "Property has been deleted."
    return jsonify({'Message': message})
