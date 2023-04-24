#!/usr/bin/python3
''' Run a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    ''' Remove the current SQLAlchemy session '''
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/', strict_slashes=False)
def states_id(id=None):
    ''' Display an HTML page with info about state, if it exists '''
    states = storage.all('State')
    if not id:
        return (render_template('7-states_list.html', states=states))

    key = 'State.{}'.format(id)
    if key in states:
        return (render_template('9-states.html', states=states[key]))
    return (render_template('9-states.html', states=None))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
