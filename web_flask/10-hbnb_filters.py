#!/usr/bin/python3
''' Run a Flask web application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    ''' Remove the current SQLAlchemy session '''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' Display a HTML page.. filter states by amenities '''
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return (render_template('10-hbnb_filters.html',
                            states=states, amenities=amenities))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
