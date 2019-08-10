import time
import json
from pprint import pprint
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

random_data = ["Some Random Data"]

@app.route('/example', methods=['GET'])
def my_lists():




    return jsonify(random_data)

app.run(debug=True)

