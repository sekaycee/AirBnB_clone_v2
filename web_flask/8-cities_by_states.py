#!/usr/bin/python3
''' Run a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    ''' Remove the current SQLAlchemy session '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' Display an HTML page.. list all States and related Cities '''
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
