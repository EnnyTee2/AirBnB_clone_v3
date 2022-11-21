#!/usr/bin/python3

from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown():
    """ Method to teardown app context """
    return storage.close()


if __name__ == "__main__":
    if getenv('HBNB_API-HOST') != none:
        hostt = getenv('HBNB_API-HOST')
    else:
        hostt = "0.0.0.0"
    if getenv('HBNB_API_PORT') != none:
        portt = int(getenv('HBNB_API_PORT'))
    else:
        portt = 5000

    app.run(host=hostt, port=portt, threaded=True)
