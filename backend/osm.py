import overpy

PARRAMATTA = {
    "name": "Parramatta",
    "s": "-33.83",
    "w": "150.99",
    "n": "-33.80",
    "e": "151.03",
    "lat": -33.82,
    "long": 151.00
}

# left=150.87 bottom=-33.81 right=150.93 top=-33.74
BLACKTOWN = {
    "name": "Blacktown",
    "s": "-33.81",
    "w": "150.87",
    "n": "-33.74",
    "e": "150.93",
    "lat": -33.78,
    "long": 150.9
}

# left=151.2 bottom=-33.9 right=151.22 top=-33.87
SURRY_HILLS = {
    "name": "Surry Hills",
    "s": "-33.9",
    "w": "151.2",
    "n": "-33.87",
    "e": "151.22",
    "lat": -38.89,
    "long": 151.2
}

# left=150.81 bottom=-33.92 right=151 top=-33.82
FAIRFIELD = {
    "name": "Fairfield",
    "s": "-33.92",
    "w": "150.81",
    "n": "-33.82",
    "e": "151.00",
    "lat": -33.88,
    "long": 150.98

}

api = overpy.Overpass()

def getSchools(area):
    result = api.query("node({}, {}, {}, {});out;".format(area["s"], area["w"], area["n"], area["e"]))
    school_list = []
    for node in result.nodes:
        if "amenity" in node.tags and node.tags["amenity"] == "school":
            if "name" in node.tags:
                school_list.append(node.tags["name"])
    return school_list

def getRestaurants(area):
    result = api.query("node({}, {}, {}, {});out;".format(area["s"], area["w"], area["n"], area["e"]))
    restaurant_list = []
    for node in result.nodes:
        if "amenity" in node.tags and (node.tags["amenity"] == "restaurant" or node.tags["amenity"] == "fast_food" or node.tags["amenity"] == "cafe"):
            if "name" in node.tags:
                restaurant_list.append(node.tags["name"])
    return restaurant_list

def getMedicalFacilities(area):
    result = api.query("node({}, {}, {}, {});out;".format(area["s"], area["w"], area["n"], area["e"]))
    med_list = []
    for node in result.nodes:
        if "amenity" in node.tags and (node.tags["amenity"] == "clinic" or node.tags['amenity'] == "doctors" or node.tags['amenity'] == "pharmacy" or node.tags['amenity'] == "dentist"):
            if "name" in node.tags:
                med_list.append(node.tags["name"])
    return med_list

def getChildcareCentres(area):
    result = api.query("node({}, {}, {}, {});out;".format(area["s"], area["w"], area["n"], area["e"]))
    cc_list = []
    for node in result.nodes:
        if "amenity" in node.tags and (node.tags["amenity"] == "childcare"):
            if "name" in node.tags:
                cc_list.append(node.tags["name"])
    return cc_list

def getPoliceStations(area):
    result = api.query("node({}, {}, {}, {});out;".format(area["s"], area["w"], area["n"], area["e"]))
    fuzz_list = []
    for node in result.nodes:
        if "amenity" in node.tags and (node.tags["amenity"] == "police"):
            if "name" in node.tags:
                fuzz_list.append(node.tags["name"])
    return fuzz_list

def getPlacesOfWorship(area):
    result = api.query("node({}, {}, {}, {});out;".format(area["s"], area["w"], area["n"], area["e"]))
    rel_list = []
    for node in result.nodes:
        if "amenity" in node.tags and (node.tags["amenity"] == "place_of_worship"):
            print(node.tags)
            if "name" in node.tags:
                rel_list.append(node.tags["name"])
    return rel_list

PLACES = [FAIRFIELD, BLACKTOWN, SURRY_HILLS, PARRAMATTA]

# for place in places:
#     print(place["name"])
#     print(getPlacesOfWorship(place))
