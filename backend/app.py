import time
import json
import sqlite3
# import database
# from database import DB_PATH
from sqlite3 import Error
from pprint import pprint
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

random_data = ["Some Random Data"]

@app.route('/example', methods=['GET'])
def my_lists():
    # lists = {}

    # # Connect to database and select all
    # conn = sqlite3.connect(DB_PATH)
    # c = conn.cursor()
    # c.execute("SELECT * FROM lists;")
    # tables = c.fetchall()
    # print(tables)
    # conn.close()



    return jsonify(random_data)

app.run(debug=True)

