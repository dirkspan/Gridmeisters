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

# read in all data
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# list for all unused houses
unused_houses = []

#set costs to 0
total_costs = 0

# shuffle houses
# r.shuffle(houses)

for house in houses:

    # dictionary voor distances
    dist_dict = {}

    # list to save distance value
    distance_list = []

    for battery in batteries:
        
        # if it fits, add house
        if battery.capacity > house.maxoutput:

            # calculate distance between house and battery
            distance = abs(house.coordinates[0] - battery.coordinates[0]) +\
                        abs(house.coordinates[1] - battery.coordinates[1])

            # add distancec to a dictionary together with the battery           
            dist_dict[battery] = distance

            # save list
            distance_list.append(distance)

        else:
            # append nothing to check it later
            distance_list.append(None)

    # if anything is none, this means that the house isn't connected yet
    if all(i is None for i in distance_list):
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

        # calculates all costs
        # costs_house = house.calc_costs(battery)
        # total_costs = total_costs + costs_house

        # if all matches found
        if len(unused_houses) == 0:
            print("all houses connected")

# prints output for all 5 batteries
for battery in batteries:

    # prints right output
    print(f"Battery {battery.id}")
    print(f"location: {battery.x,battery.y}")
    print(f"capacity: 1507.0")
    print(f"houses:")

    # find all coordinates for the route
    for house in battery.houses_to_battery:

        current_x = house.x
        end_x= battery.x
        current_y = house.y
        end_y = battery.y
            
        if current_y < end_y:
            while current_y < end_y:
                house.cables.append((current_x, current_y))
                current_y += 1

        elif current_y > end_y:
            while current_y > end_y:
                house.cables.append((current_x, current_y))
                current_y -= 1

        if current_x < end_x:
            while current_x <= end_x:
                house.cables.append((current_x, current_y))
                current_x += 1

        elif current_x > end_x:
            while current_x >= end_x:
                house.cables.append((current_x, current_y))
                current_x -= 1
        # house.coordinates_cables(battery)
            
        # prints output for each house, each coordinate of the cable
        print(f"house ID: {house.id}")
        print(f"location: {house.x,house.y},")
        print(f"output: {house.maxoutput},")
        print(f"cables:{house.cables}")

# prints total costs, last status. 
# print('Total costs in the end:')
# print(total_costs) 




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
