"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""

import load_data
import house
import battery
import cables 
import random as r

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# huizen die niet gebruikt worden
unused_houses = []

#set costs and route to 0
# house.routetest = []
costs = 0

# shuffle huizen
r.shuffle(houses)

for house in houses:

    # dictionary voor distances
    dist_dict = {}

    # lijst om waarde bij te houden, weet niet zo goed hoe dit met dict werkt, vandaar lijst erbij gedaaan
    distance_list = []

    for battery in batteries:
        
        # kan geconnect worden
        if battery.capacity > house.maxoutput:

            # reken distance uit tussen batt en huis    
            distance = abs(house.coordinates[0] - battery.coordinates[0]) +\
                        abs(house.coordinates[1] - battery.coordinates[1])

            # voeg distance tot aan batterij toe met batterij            
            dist_dict[battery] = distance

            # hou lijst bij
            distance_list.append(distance)

        else:
            # append niks zodat we deze conditie later kunnen checken
            distance_list.append(None)

    # als alles None is betekent dat het huis niet gebruikt wordt (voor nu)
    if all(i is None for i in distance_list):
        unused_houses.append(house)

    else:
        # dichtsbijzijnde afstand is minimale value
        closest_distance = min(dist_dict.items(), key=lambda x: x[1])

        # is key van minimale value, dus de batterij
        closest_battery= closest_distance[0]
        battery = closest_battery

        # rekent route uit
        route = (house.x, battery.y)

        # connect huis aan batterij en vice versa
        house.connect_to_battery = battery
        battery.connect_house(house)

        # costs_house = house.calc_costs(battery)
        # costs = costs + costs_house

        # we hebben alle matches gevonden
        if len(unused_houses) == 0:
            break

# print uitkomst voor alle 5 batterijen
for battery in batteries:

    # print(f"This is battery {battery.id} Houses: {battery.temp_houses_to_battery}")
    print(f"NEW BATTERY!!")
    print(f"location: {battery.x,battery.y}")
    print(f"capacity: 1507.0")
    print(f"houses:")

    for house in battery.houses_to_battery:
        house.coordinates_cables(battery)
        print(house.cables)
            
        # prints output for each house, each coordinate of the cable
        print(f"house ID: {house.id}")
        print(f"location: {house.x,house.y},")
        print(f"output: {house.maxoutput},")
        print(f"cables:{house.cables}")

# prints total costs, last status. 
# print('Total costs in the end:')
# print(costs) 




# # Loop to plot coordinates batteries
# i = -1
# for battery in batteries:
#     i += 1
#     for house in battery.houses_to_battery:

#         # print(battery.houses_to_battery)
#         # for battery in batteries:
#         colors = ['r', 'k', 'b', 'g', 'c']

#         house_x = house.x
#         house_y = house.y

#         battery_x = battery.x
#         battery_y = battery.y

#         cutting_point_x = house.x
#         cutting_point_y = battery.y

#         #plot line between house and cutting point 
#         x = [house_x, cutting_point_x, battery_x]
#         y = [house_y, cutting_point_y, battery_y]

#         ax = plt.subplot(111)

#         houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
#         batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

#         plt.plot(x,y, color= colors[i])

# plt.savefig("4plot.png")
