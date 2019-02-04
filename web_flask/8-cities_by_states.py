#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' Returns an HTML page with cities and states '''
    storage.reload()
    states = storage.all("State")
    states_list = []
    for k, v in states.items():
        states_list.append(v)
    return render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def teardown(exception):
    ''' Closes the database '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
