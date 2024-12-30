import json 
from geopy.distance import geodesic

with open("export.geojson", 'r') as f:
    data = json.load(f)

museums = [feature for feature in data['features'] if feature['type'] == "Feature" and "tourism" in feature['properties'] and feature['properties']['tourism'] == "museum"]

libraries = [feature for feature in data['features'] if feature['type'] == "Feature" and "amenity" in feature['properties'] and feature['properties']['amenity'] == "library"]


for museum in museums:
    museum_coords = tuple(museum['geometry']['coordinates'])
    #print(museum_coords)
    #print(museum_coords)
    for library in libraries:
        library_coords = tuple(library['geometry']['coordinates'])
        #print(library_coords)
        dist = int(geodesic(museum_coords, library_coords).km*1000)
        #print(dist)

        print(f"{museum['properties']['name']} -> {library['properties']['name']} -> {dist}") 

# c1 = (5.7423562, 45.0968926)
# print(c1)
# c2 = (17.1067753, 48.1463115)
# print(geodesic(c1, c2).km)