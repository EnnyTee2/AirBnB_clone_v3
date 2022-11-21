#!/usr/bin/python3
""" Index """
from models.state import State
from api.v1.views import app_views
from flask import jsonify, make_response, request
from models import storage
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """ Method to retrieve list of all states """
    all_states = storage.all('State').values()
    state_list = []
    for state in all_states:
        state_list.append(state.to_dict())
    return jsonify(state_list)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """ Method to retrieve a specific state by id """
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    return jsonify(state.to_dict())
