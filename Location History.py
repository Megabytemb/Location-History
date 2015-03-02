import json
from geopy.distance import great_circle

data = json.loads(open("C:\data\LocationHistory.json").read())

print_counter = 0
total = 0
curr_p = (data["locations"][0]["latitudeE7"] * 0.0000001,data["locations"][0]["longitudeE7"] * 0.0000001)
prev_p = (data["locations"][1]["latitudeE7"] * 0.0000001,data["locations"][1]["longitudeE7"] * 0.0000001)

for location in data["locations"]:
    curr_p = (location["latitudeE7"] * 0.0000001,location["longitudeE7"] * 0.0000001)
    total += great_circle(curr_p, prev_p).kilometers
    if print_counter > 5000:
        print total
        print_counter = 0
    print_counter +=1
    prev_p = curr_p
