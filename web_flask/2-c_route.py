#!/usr/bin/python3
''' Run a Flask web application '''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Call with / route.. display HELLO HBNB '''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Call with /hbnb route.. display HBNB '''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' Call with /c/ route.. display C with text value '''
    return ('C %s' % text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
