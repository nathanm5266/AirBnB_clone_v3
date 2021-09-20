#!/usr/bin/python3
"""
status of the app_route views
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status")
def statsu():
    """
    check status route
    """
    return jsonify({"status": "OK"})
