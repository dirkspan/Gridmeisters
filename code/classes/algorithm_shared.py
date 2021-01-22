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

# # list for all unused houses
# unused_houses = []

# #set costs to 0
# costs = 0

# shuffle houses
random.shuffle(houses)

 # empty list of coordinates
cables_coordinates = []

for battery in batteries:
    cables_coordinates.append(battery.coordinates)


print(cables_coordinates)

for house in houses:

    print(house.x)
    print(house.y)
    connect_options = []

    # keep track of distances between each house and battery
    dist_dict = {}

    # keeps track on wether battery is useable
    keep_track = []

    for tuple in cables_coordinates:
        distance = int(abs(house.coordinates[0] - tuple[0]) + abs(house.coordinates[1] - tuple[1]))
        connect_options.append(distance)

        dist_dict[tuple] = distance

    # return closest distance of a house to the battery
    closest_distance = min(dist_dict.items(), key=lambda x: x[1])

    closest_connection = closest_distance[0]

    print(f"id: {house.id}")
    print(f"closest_connection {closest_connection}")

    connection = closest_connection

    route = (house.x, connection[1])

    # start is house, end is battery
    current_x = house.x
    end_x= connection[0]
    current_y = house.y
    end_y = connection [1]

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
        if tuple not in cables_coordinates:
            cables_coordinates.append(tuple)
            print(tuple)

# costs calculation
number_of_cables = number_of_cables = int(len(cables_coordinates))

costs_all_cables = number_of_cables * 9
print(f"costs all cables: {costs_all_cables}")
costs = costs_all_cables + (5000 * len(batteries))
print(f"all costs for complete district: {costs} ")

#     for battery in batteries:
        
#         # battery is not full
#         if battery.status(house) == True:

#             distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

#             dist_dict[battery] = distance

#             # save list
#             keep_track.append(1)

#         else:
#             keep_track.append(0)

#     if keep_track.count(1) == 0:
        
#         # battery is full, append house to list of unused houses    
#         unused_houses.append(house)

#     else:

#         # return closest distance of a house to the battery
#         closest_distance = min(dist_dict.items(), key=lambda x: x[1])


#         closest_battery= closest_distance[0]
#         battery = closest_battery

#         route = (house.x, battery.y)

#         # connects house to battery and vice versa
#         house.connect_to_battery = battery
#         battery.connect_house(house)

        

# # we hebben alle matches gevonden
# # if len(unused_houses) == 0:

# # print uitkomst voor alle 5 batterijen
# for battery in batteries:

#     # print(f"This is battery {battery.id} Houses: {battery.temp_houses_to_battery}")
#     print(f"NEW BATTERY!!")
#     print(f"location: {battery.x,battery.y}")
#     print(f"capacity: 1507.0")

#     for house in battery.houses_to_battery:

#         # cable.coordinates_cables(house, battery)

#         
#         # prints output for each house, each coordinate of the cable
#         print(f"house ID: {house.id}")
#         print(f"location: {house.x,house.y},")
#         print(f"output: {house.maxoutput},")
#         print(f"cables:{house.cables}")  