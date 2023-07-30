#!/usr/bin/python3
""" index within views """
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"amenities": Amenity, "cities": City,
        "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/status')
def views_status():
    """ return status of views """
    return ({"status": "OK"})

@app_views.route('/stats')
def object_stats():
    """ return states of each object type """
 
    results = {}
    for key, value in classes.items():
        results[key] = storage.count(value)
    return (results)
