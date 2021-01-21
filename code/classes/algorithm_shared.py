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

# shuffle houses
random.shuffle(houses)

# empty list of coordinates
cables_coordinates = []

# first add the batties as connect option
for battery in batteries:
    cables_coordinates.append(battery.coordinates)

# loop for house in houses
for house in houses:

    # empty list for connect options 
    connect_options = []

    # keep track of distances between each house and battery
    dist_dict = {}

    # for all connect options calculate distance to house and save in list
    for tuple in cables_coordinates:
        distance = int(abs(house.coordinates[0] - tuple[0]) + abs(house.coordinates[1] - tuple[1]))
        connect_options.append(distance)

        # add all connect options to distance dictionary
        dist_dict[tuple] = distance

    # return closest distance of a house to all connect optionss
    closest_distance = min(dist_dict.items(), key=lambda x: x[1])
    closest_connection = closest_distance[0]
    connection = closest_connection
    
    # define route
    route = (house.x, connection[1])

    # start is house, end is connection coordinates
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

    # print whole route from house to connection point
    # print(house.cables)

    # for all coordinates in the route check if there is a cable already other wise append route
    for tuple in house.cables:
        if tuple not in cables_coordinates:
            cables_coordinates.append(tuple)

    # print output, house id, coordinates and coordinates of closest item
    print(f"id: {house.id}")
    print(f"house: ({house.x}, {house.y})")
    print(f"closest_connection: {closest_connection}")

# cable costs calculation, calculate costs for all grid segments, so its min start point battery
number_of_cables = number_of_cables = int(len(cables_coordinates))
costs_all_cables = (number_of_cables * 9) - len(batteries)*9
print(f"costs all cables: {costs_all_cables}")

# add the costs for the battaries
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