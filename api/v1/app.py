#!/usr/bin/python3
""" Flask Application that runs based on an imported Blueprint """
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv



app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(error):
    """ Method to teardown app context """
    storage.close()


""" Main Application """
if __name__ == "__main__":
    hostt = getenv('HBNB_API_HOST')
    portt = getenv('HBNB_API_PORT')
    
    hostt = '0.0.0.0' if not hostt else HBNB_API_HOST
    portt = 5000 if not portt else HBNB_API_PORT
    app.run(host=hostt, port=portt, threaded=True)
