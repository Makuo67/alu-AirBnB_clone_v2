#!/usr/bin/python3

"""Starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Comment"""
    from models import storage
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
