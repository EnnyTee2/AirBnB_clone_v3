#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def all_states():
    """ Method to retrieve list of all states """
    all_states = storage.all('State')
    return jsonify(all_states)
