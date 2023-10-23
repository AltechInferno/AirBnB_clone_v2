#!/usr/bin/python3
""" launches an app with Flask framework """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """/ route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """/c/<text> route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """/python/<text> route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """/number/<n> route """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """/number_template/<n> route """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """/number_template/<n> route """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
