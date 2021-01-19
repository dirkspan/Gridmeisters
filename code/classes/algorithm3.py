"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""

import load_data
import house
import battery
import random as r
import matplotlib.pyplot as plt


reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# huizen die niet gebruikt worden
unused_houses = []

for house in houses:

    # dictionary voor distances
    dist_dict = {}

    # lijst om waarde bij te houden
    keep_track = []

    for battery in batteries:
        
        # kan geconnect worden
        if battery.capaciteit > house.maxoutput:

            # reken distance uit tussen batt en huis    
            distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

            # voeg distance tot aan batterij toe met batterij            
            dist_dict[battery] = distance

            # hou lijst bij
            keep_track.append(1)

        else:
            #  deze conditie wordt later gecheckt
            keep_track.append(0)

    if all(i == 0 for i in keep_track):
        unused_houses.append(house)

    else:
        # dichtsbijzijnde afstand is minimale value
        closest_distance = min(dist_dict.items(), key=lambda x: x[1])

        # is key van minimale value, dus de batterij
        closest_battery= closest_distance[0]
        battery = closest_battery

        # rekent route uit
        house.route = (house.x, battery.y)

        # connect huis aan batterij en vice versa
        house.connect_to_battery = battery
        battery.connect_house(house)
        house.calc_costs(battery)

        # alle matches gevonden
        if len(unused_houses) == 0:

            # print uitkomst voor alle 5 batterijen, let alleen op de laatste 5 uitkomsten
            # omdat hij hier blijft loopen
            for battery in batteries:
                print(len(battery.temp_houses_to_battery))
                # print(f"this is: {battery}: Houses: {battery.temp_houses_to_battery}") 


                