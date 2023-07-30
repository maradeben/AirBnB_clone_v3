#!/usr/bin/python3
""" index within views """
from api.v1.views import app_views


@app_views.route('/status')
def views_status():
    """ return status of views """
    return ({"status": "OK"})
