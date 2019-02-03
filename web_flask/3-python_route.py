#!/usr/bin/python3
''' Script that starts a Flask web application '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    ''' Returns a phrase '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Returns phrase "HBNB" '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' Returns a phrase starting with "C" '''
    return ("C " + text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    ''' Returns a phrase starting with "Python" '''
    return ("Python " + text.replace("_", " "))


if __name__ == '__main__':
    app.run()
