#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Returns an HTML page '''
    states = storage.all("State")
    states_list = []
    for k, v in states.items():
        states_list.append(v)
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def teardown(exception):
    ''' Closes the database '''
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
