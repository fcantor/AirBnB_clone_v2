#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def show_state_cities(state_id=None):
    """ """
    data = storage.all('State')
    states = []
    target = None
    for k, v in data.items():
        states.append(v)
        if state_id == v.id:
            target = v

    return render_template('9-states.html', states=states,
                           target=target, state_id=state_id)

@app.teardown_appcontext
def remove_session(response_or_exc):
    ''' Closes current storage '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
