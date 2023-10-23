#!/usr/bin/python3
"""launches a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exc):
    """closes
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """outputing an HTML page
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
