"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""
import load_data
import house
import battery
import random
import matplotlib.pyplot as plt

from matplotlib import style

# read in all data
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# shuffle houses
random.shuffle(houses)

# empty list of coordinates
cables_coordinates = []


# first add the batties as connect option
for battery in batteries:
    cables_coordinates.append(battery.coordinates)

bat_dict = {}

# loop for house in houses
for house in houses:

    # empty list for connect options 
    connect_options = []

    # keep track of distances between each house and battery
    dist_dict = {}

    # for all connect options calculate distance to house and save in list
    for cable_point in cables_coordinates:
        distance = int(abs(house.coordinates[0] - cable_point[0]) + abs(house.coordinates[1] - cable_point[1]))
        connect_options.append(distance)

        # add all connect options to distance dictionary
        dist_dict[cable_point] = distance


    # return closest distance of a house to all connect optionss
    closest_distance = min(dist_dict.items(), key=lambda x: x[1])
    closest_connection = closest_distance[0]

    # als er nog plek is!!
    # 

    connection = closest_connection

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
    
    # dictionary with battery coupeled.
    for battery in batteries:
        if connection == battery.coordinates:
            house.connected_to = battery.id
            print("batterij ID")
            print(house.connected_to)
            for cable_point in cables_coordinates:
                bat_dict[cable_point] = house.connected_to
        else:
            pass
    
    #loop trough dictionary     
    for item in bat_dict:
        for cable_point in house.cables:

            # find connection point in dictionary 
            if cable_point == item:
                print(f"houseID: {house.id} coordiante connection: {item}")

                # get coupeled id of this cable grid
                batitem = bat_dict.get(item)

                # add same connected battery as connectedbattery of connected grid piece
                house.connected_to = batitem
                print(f"battery connected to: {house.connected_to}")

                # if it is a new coordinate add to dictionary with right connected battery and add to cables_Coordinates
                for tuple in house.cables:
                    if tuple not in cables_coordinates:
                        cables_coordinates.append(tuple)
                        bat_dict[cable_point] = house.connected_to          
    

# print output, house id, coordinates and coordinates of closest item
print(f"id: {house.id}")
print(f"house: ({house.x}, {house.y})")
print(f"closest_connection: {closest_connection}")

# cable costs calculation, calculate costs for all grid segments, so its min start point battery
number_of_cables = number_of_cables = int(len(cables_coordinates))
costs_all_cables = (number_of_cables * 9) - len(batteries)*9
print(f"costs all cables: {costs_all_cables}")