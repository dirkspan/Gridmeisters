"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""

import load_data
import house
import battery
import cables 
import random
import matplotlib.pyplot as plt


# read in all data
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# list for all unused houses
unused_houses = []

# shuffle houses
random.shuffle(houses)

for house in houses:

    # keep track of distances between each house and battery
    dist_dict = {}

    # keeps track on wether battery is useable
    keep_track = []

    for battery in batteries:
        
        # battery is not full
        if battery.status(house) == True:

            distance = abs((house.coordinates[0] - battery.coordinates[0]) + (house.coordinates[1] - battery.coordinates[1]))

            dist_dict[battery] = distance

            keep_track.append(1)

        else:
            keep_track.append(0)

    if keep_track.count(1) == 0:
        
        # battery is full, append house to list of unused houses    
        unused_houses.append(house)

    else:

        # return closest distance of a house to the battery
        closest_distance = min(dist_dict.items(), key=lambda x: x[1])

        closest_battery= closest_distance[0]
        battery = closest_battery

        route = (house.x, battery.y)

        # connects house to battery and vice versa
        house.connect_to_battery = battery
        battery.connect_house(house)
        house.calc_costs(battery)
        battery.coordinates_cables(battery)

        # all matches found, not a single house unused
        if unused_houses == []:

            for battery in batteries:

                # print(len(battery.houses_to_battery))
                print(f"{battery}: Houses: {len(battery.temp_houses_to_battery)}")