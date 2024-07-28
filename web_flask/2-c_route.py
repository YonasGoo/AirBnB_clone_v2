#!/usr/bin/python3
"""starts a Flask web app"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """Return 2 words"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Return a word"""
    return "HBNB"


@app.route('/c/<subpath>', strict_slashes=False)
def route_c(subpath):
    """Return subpath"""
    return "C {}".format(escape(subpath).replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
