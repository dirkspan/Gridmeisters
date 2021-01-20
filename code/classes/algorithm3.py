"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""

import load_data
import house
import battery
import cables 
import random as r
import matplotlib.pyplot as plt


# read in all data
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# list for all unused houses
unused_houses = []

#set costs to 0
total_costs = 0

for house in houses:

    # dictionary voor distances
    dist_dict = {}

    # lijst om waarde bij te houden
    keep_track = []

    for battery in batteries:
        

        if battery.capacity > house.maxoutput:

            # reken distance uit tussen batt en huis    
            distance = abs((house.coordinates[0] - battery.coordinates[0]) + (house.coordinates[1] - battery.coordinates[1]))

            # add distance to a dictionary together with the battery           
            dist_dict[battery] = distance

            keep_track.append(1)

        else:
            #  deze conditie wordt later gecheckt
            keep_track.append(0)

    if keep_track.count(1) == 0:
        unused_houses.append(house)

    else:

        # closest battery is the minimum value
        closest_distance = min(dist_dict.items(), key=lambda x: x[1])

        # the id of the minimum value, closest battery
        closest_battery= closest_distance[0]
        battery = closest_battery

        # calculates route
        route = (house.x, battery.y)

        # connect the house the battery and connect the battery to the house 
        house.connect_to_battery = battery
        battery.connect_house(house)
        house.calc_costs(battery)
        battery.coordinates_cables(battery)

        # alle matches gevonden
        if not unused_houses:

            for battery in batteries:

                print(len(battery.houses_to_battery))
                # print(f"this is: {battery}: Houses: {battery.temp_houses_to_battery}") 