#!/usr/bin/python3
""" Blueprint for API """

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint(url_prefix="/api/v1")
