"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""
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

# house = houses[0]

for house in houses:

    # keep track of distances between each house and battery
    dist_dict = {}

    # keeps track on wether battery is useable
    keep_track = []

    # empty list of coordinates
    cables_coordinates = []

    for battery in batteries:
        
        # battery is not full
        if battery.status(house) == True:

            distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

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

        

# we hebben alle matches gevonden
# if len(unused_houses) == 0:

# print uitkomst voor alle 5 batterijen
for battery in batteries:

    # print(f"This is battery {battery.id} Houses: {battery.temp_houses_to_battery}")
    print(f"NEW BATTERY!!")
    print(f"location: {battery.x,battery.y}")
    print(f"capacity: 1507.0")

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

        for tuple in house.cables:
            # line_house = house.cables
            if tuple not in cables_coordinates:
                cables_coordinates.append(tuple)

        number_of_cables = int(len(cables_coordinates))
        costs_all_cables_to_battery = number_of_cables * 9 
  

        # prints output for each house, each coordinate of the cable
        print(f"house ID: {house.id}")
        print(f"location: {house.x,house.y},")
        print(f"output: {house.maxoutput},")
        print(f"cables:{house.cables}")

    print("cable costs, cables shared:")
    print(costs_all_cables_to_battery)

    # costs for all batteries
    costs = costs_all_cables_to_battery + (5000 * len(batteries))
    print(f"all costs for complete district: {costs} ")
    
        
        

    # print("all used coordinates")
    # print(cables_coordinates)

    
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

        # line_house

        #plot line between house and cutting point 
        # x = [house_x, cutting_point_x, battery_x]
        # y = [house_y, cutting_point_y, battery_y]

        ax = plt.subplot(111)

        houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
        batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')
    # all matches found, not a single house unused
    if unused_houses == []:
        # print(f"{battery}: Houses: {len(battery.temp_houses_to_battery)}")

        plt.plot(line_house, color= colors[i])

# plt.savefig("test3share.png")
for house in houses:
    plt.plot(*zip(*house.cables))
plt.savefig("test3share.png")
