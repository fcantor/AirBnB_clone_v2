#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def show_state_cities(state_id=None):
    ''' Returns an HTML page of specific state with cities '''
    obj = storage.all('State')
    states_list = []
    state  = None
    for k, v in obj.items():
        states_list.append(v)
        if state_id == v.id:
            state = v
    return render_template('9-states.html', states_list=states_list,
                           state=state, state_id=state_id)


@app.teardown_appcontext
def remove_session(response_or_exc):
    ''' Closes current storage '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
