#!/usr/bin/python3
"""launches a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """prints Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """prints C and value of the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_magic(text='is cool', strict_slashes=False):
    """prints python and value of the text
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """prints n is a number if n is an integer
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """print an HTML page if n is an integer
    """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
