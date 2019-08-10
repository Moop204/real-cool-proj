import time
import json
import overpass
import osm
from osm import PLACES
# FAIRFIELD, BLACKTOWN, SURRY_HILLS, PARRAMATTA
from pprint import pprint
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# api = overpass.API(endpoint="https://lz4.overpass-api.de/api/interpreter")

app = Flask(__name__)


@app.route('/main', methods=['GET', 'POST'])
def my_lists():
    if request.method == "POST":
        data = request.json
        location = data["place"]
        
        QUERY = {}
        if (location == "Parramatta"):
            QUERY = osm.PARRAMATTA
        elif (location == "Fairfield"):
            QUERY = osm.FAIRFIELD
        elif (location == "Blacktown"):
            QUERY = osm.BLACKTOWN
        elif (location == "Surry Hills"):
            QUERY = osm.SURRY_HILLS
        
        amenities = osm.getAmenities(QUERY)
        
        schools = osm.getSchools(amenities)
        restaurants = osm.getRestaurants(amenities)
        med = osm.getMedicalFacilities(amenities)
        cc = osm.getChildcareCentres(amenities)
        police = osm.getPoliceStations(amenities)
        worship = osm.getPlacesOfWorship(amenities)
        
        result = {
            "location": QUERY["name"],
            "amenities": {
                "schools": {"list": schools, "size": len(schools)},
                "restaurants": {"list":restaurants, "size": len(restaurants)},
                "medical": {"list": med, "size": len(med)},
                "childcare": {"list": cc, "size": len(cc)},
                "police": {"list": police, "size": len(police)},
                "worship": {"list": worship, "size": len(worship)}
            }    
        }
    
    return jsonify(result)

app.run(debug=True)

#