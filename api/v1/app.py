#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(error):
    """ Method to teardown app context """
    storage.close()


if __name__ == "__main__":
    if getenv('HBNB_API_HOST') != none:
        hostt = getenv('HBNB_API_HOST')
    else:
        hostt = '0.0.0.0'
    if getenv('HBNB_API_PORT') != none:
        portt = getenv('HBNB_API_PORT'))
    else:
        portt = '5000'

    app.run(host=hostt, port=portt, threaded=True)
