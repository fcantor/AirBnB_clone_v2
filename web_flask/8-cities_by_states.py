#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_states():
    ''' Returns an HTML page showing states and its cities '''
    obj = storage.all('State')
    states_list = []
    for k, v in obj.items():
        states_list.append(v)
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def remove_session(exception):
    ''' Closes the current storage session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
