#!/usr/bin/python3
''' Run a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    ''' Remove the current SQLAlchemy session '''
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    ''' Display an HTML page with info about state, if it exists '''
    states = storage.all('State').values()
    if not id:
        return (render_template('9-states.html', states=states))
    for state in states:
        if state.id == id:
            return (render_template('9-states.html', state=state))
    return (render_template('9-states.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
