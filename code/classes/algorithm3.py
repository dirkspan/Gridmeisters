"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""
import pickle

import load_data
import house
import battery
import cables 
import random
import matplotlib.pyplot as plt

from matplotlib import style

# read in all data
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# list for all unused houses
unused_houses = []

#set costs to 0
costs = 0

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

<<<<<<< HEAD
            distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])
=======
            distance = abs((house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1]))
>>>>>>> 7fbd364f9fcd5a641c7a1fd79698730ea71c2c75

            dist_dict[battery] = distance

            # save list
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

        # calculates house costs and add it to the total
        costs_house = house.calc_costs(battery)
        costs = costs + costs_house
        
        # if not unused_houses:
        #     for battery in batteries:
        #         print(f"{battery} with houses: {battery.temp_houses_to_battery}")

# we hebben alle matches gevonden
if len(unused_houses) == 0:

    # print uitkomst voor alle 5 batterijen
    for battery in batteries:

        # print(f"This is battery {battery.id} Houses: {battery.temp_houses_to_battery}")
        print(f"NEW BATTERY!!")
        print(f"location: {battery.x,battery.y}")
        print(f"capacity: 1507.0")
        print(f"houses:")

        for house in battery.houses_to_battery:

            # cable.coordinates_cables(house, battery)

            # start is house, end is battery
            current_x = house.x
            end_x= battery.x
            current_y = house.y
            end_y = battery.y

            # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
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
           
            # prints output for each house, each coordinate of the cable
            print(f"house ID: {house.id}")
            print(f"location: {house.x,house.y},")
            print(f"output: {house.maxoutput},")
            print(f"cables:{house.cables}")

    # costs for all batteries
    costs += 5000 * len(batteries)

    # total costs for cables and batteries
    print('Total costs in the end:', costs) 


else: 
    print("No solution")


for battery in batteries:
    list_x_values = []
    for house in battery.houses_to_battery:
        list_x_values.append(house.x)
        
        max_x = max(list_x_values)
        min_x = min(list_x_values) 
        # costs horizontaal
        cable_costs= (max_x - min_x) * 9

        # costs verticaal 
        cable_costs_vertically = []

    for battery in batteries:
        for house in battery.houses_to_battery:
            list_horizontal_values = []
            if house.x == battery.houses_to_battery[i].x:
            try:
                cable_costs += abs(house.y - battery.y) * 9
            except house.x == otherhouse.x

                cable_costs += abs(house.y that has biggest difference - battery.y) * 9


    print(list_x_values)
    print("battery:", battery.id)
    print("max:", max_x)
    print("min:", min_x)
    print("cable_costs when shared:", cable_costs)
    print("\n")
    # ========================================================================================================

# for battery in batteries:
#     list_x_values = []
#     for house in battery.houses_to_battery:
#         list_x_values.append(house.x)
        
#         max_x = max(list_x_values)
#         min_x = min(list_x_values) 
#         # costs horizontaal
#         cable_costs_horizontally = (max_x - min_x) * 9

#         # costs verticaal 
#         cable_costs_verticaly = []
#     for battery in batteries:
#         for house in battery.houses_to_battery:
#             cable_costs_verticaly_1= abs(house.y - battery.y)
#             print(house.y, battery.y)
#             print(cable_costs_verticaly_1)
#             print("=======================")

#     print(list_x_values)
#     print("battery:", battery.id)
#     print("max:", max_x)
#     print("min:", min_x)
    
#     print(cable_costs_horizontaly)
#     print("\n")



# Loop to plot coordinates batteries
i = -1
for battery in batteries:
    i += 1
    for house in battery.houses_to_battery:

        colors = ['c', 'k', 'b', 'g', 'r']

        house_x = house.x
        house_y = house.y

        battery_x = battery.x
        battery_y = battery.y

        cutting_point_x = house.x
        cutting_point_y = battery.y

        #plot line between house and cutting point 
        x = [house_x, cutting_point_x, battery_x]
        y = [house_y, cutting_point_y, battery_y]

        ax = plt.subplot(111)

        houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
        batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')
        # all matches found, not a single house unused
    if unused_houses == []:
        print(f"{battery}: Houses: {len(battery.temp_houses_to_battery)}")

        plt.plot(x,y, color= colors[i])

<<<<<<< HEAD
# plt.savefig("4plot.png")
                # print(len(battery.houses_to_battery))

=======
plt.savefig("4plot.png")
print(len(battery.houses_to_battery))
>>>>>>> 7fbd364f9fcd5a641c7a1fd79698730ea71c2c75
