#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Method to return app status """
    return jsonify(status='OK')


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    Method to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
            }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
