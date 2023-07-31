#!/usr/bin/python3
""" containing the state view """

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request


@app_views.route('/states/', methods=['GET'])
def get_all_states():
    '''Retrieves a list of all State objects'''
    states_list = [obj.to_dict() for obj in storage.get(State).values()]
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_id_state(state_id):
    """ get a state with the given id """
    the_state = storage.get(State, state_id).to_dict()
    if the_state:
        return jsonify(the_state)
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_id_state(state_id):
    """ delete the state with given id """
    states_list = storage.get(State).values()
    to_del = [obj.to_dict() for obj in states_list if obj.id == state_id]
    if to_del == []:
        abort(404)
    for obj in states_list:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    """ create and add a new state """
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ update a state object """
    states_list = storage.get(State).values()
    the_state = [obj.to_dict() for obj in states_list if obj.id == state_id]
    if not the_state:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    the_state['name'] = request.json['name']
    for obj in states_list:
        if obj.id == state_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state_obj[0]), 200
