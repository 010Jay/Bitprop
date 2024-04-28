import json

from types import SimpleNamespace

from repository.AgentRepository import AgentRepository

from flask import jsonify, request, Blueprint

agent_api = Blueprint('agent_api', __name__)
db = AgentRepository()


@agent_api.route('/agent/readAll', methods=['GET'])
def get_agents():
    agent_list = db.read_all()
    return jsonify({'agents': agent_list})


@agent_api.route('/agent/read/<agent_id>', methods=['GET'])
def get_user(agent_id):
    agent = db.read(agent_id)
    return jsonify({'agent': agent})


@agent_api.route('/agent/create', methods=['POST'])
def create_agent():
    data = json.dumps(request.json)
    agent = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    db.create(agent)
    return jsonify({'agent': request.json})


@agent_api.route('/agent/delete/<agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    db.delete(agent_id)
    message = "Agent has been deleted."
    return jsonify({'Message': message})


