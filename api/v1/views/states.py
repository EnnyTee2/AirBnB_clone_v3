#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """ Method to retrieve list of all states """
    all_states = storage.all('State').values()
    state_list = []
    for state in all_states:
        state_list.append(state.to_dict())
    return jsonify(state_list)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def all_states(state_id):
    """ Method to retrieve list of a specific state by id """
    statey = storage.get('State', state_id)
    return jsonify(statey)
