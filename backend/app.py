import time
import json
import overpass
import osm
from osm import PLACES
# FAIRFIELD, BLACKTOWN, SURRY_HILLS, PARRAMATTA
from pprint import pprint
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

api = overpass.API(endpoint="https://lz4.overpass-api.de/api/interpreter")


app = Flask(__name__)

random_data = ["Some Random Data"]

@app.route('/main', methods=['GET'])
def my_lists():
    worships = osm.getPlacesOfWorship(osm.SURRY_HILLS)

    return jsonify(worships)

app.run(debug=True)

#