import overpass 
api = overpass.API(endpoint="https://lz4.overpass-api.de/api/interpreter")

response = api.get('node["name"="Gielgen"]')
print(response)

shop_count = 0
for feature in response["features"]:
    if "shop" in feature["properties"]:
        shop_count += 1
print(shop_count)

#print( [(feature['tags']) for feature in response["features"]] )