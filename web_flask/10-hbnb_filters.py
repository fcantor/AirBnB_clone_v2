#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' Displays an HTML page with website filters '''
    obj = storage.all("State")
    states_list = [v for k, v in obj.items()]
    obj = storage.all("Amenity")
    amenities_list = [v for k, v in obj.items()]
    return render_template('10-hbnb_filters.html',
                           states_list=states_list,
                           amenities_list=amenities_list)


@app.teardown_appcontext
def remove_session(response_or_exc):
    ''' Closes current storage '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
