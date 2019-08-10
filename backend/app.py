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
app.run()