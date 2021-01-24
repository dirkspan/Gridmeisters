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
# random.shuffle(houses)

# empty list of coordinates
cables_coordinates = []

temp_houses_to_battery = []

bat_dict = {}

unused_houses = []


# first add the batteries as connect option
for battery in batteries:
    cables_coordinates.append(battery.coordinates)

# set count for connected houses to 0
count_houses = 0

# loop for house in houses
for house in houses:
    print(house.id)   

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

    connection = closest_connection
    
    # dictionary with battery coupeled.
    for battery in batteries:
        if connection == battery.coordinates:
            # if battery.status(house) == True:
            battery.houses_to_battery.append(house)
            battery.connect_house(house)
            print(battery.capacity)
            house.connected_to = battery.id
            for cable_point in cables_coordinates:
                bat_dict[cable_point] = house.connected_to

    # start is house, end is connection coordinates
    current_x = house.x
    print(current_x)
    end_x= connection[0]
    print(end_x)
    current_y = house.y
    print(current_y)
    end_y = connection [1]
    print(end_y)

    # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
    if current_y < end_y:
        while current_y <= end_y:
            house.cables.append((current_x, current_y))
            current_y += 1

    elif current_y > end_y:
        while current_y >= end_y:
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

    if house.coordinates == connection:
        battery.connect_house(house)

    for tuple in house.cables:
                    if tuple not in cables_coordinates:
                        cables_coordinates.append(tuple)
                        bat_dict[cable_point] = house.connected_to

    print("check3")
    print(house.cables)

    for i in house.cables:
        if i == (len(house.cables)-1): 
            print ("The last element of list using loop : "+  str(house.cables[i]))
    #loop trough dictionary 
    #  = len(house.cables)
    house.cables.reverse() 
# print("The last element of list using reverse : "
#                             +  str(test_list[0]))
#         if i == 
    # connection_point = house.cables[len-1]   
    # print(connection_point) 
    for item in bat_dict:
        if house.coordinates == item:
            battery.connect_house(house)
        
            print(f"houseID: {house.id} coordiante connection: {item}")

            # get coupeled id of this cable grid
            batitem = bat_dict.get(item)

            # add same connected battery as connectedbattery of connected grid piece
            house.connected_to = batitem

            print(f"number of houses connected to battery {battery.id}: {len(battery.houses_to_battery)}")

        for cable_point in house.cables:
            # find connection point in dictionary 
            if cable_point == item:
                print("verbind")
                battery.connect_house(house)
                print(f"houseID: {house.id} coordiante connection: {item}")

                # get coupeled id of this cable grid
                batitem = bat_dict.get(item)

                # add same connected battery as connectedbattery of connected grid piece
                house.connected_to = batitem

                # for battery in batteries:
                #     if battery.id == batitem:
                #         if battery.status(house) == True:
                #             print("test")
                #             battery.houses_to_battery.append(house)
                print(f"number of houses connected to battery {battery.id}: {len(battery.houses_to_battery)}")

                            # capacity of battery
                            # print(battery.capacity)
                            # battery.capacity = battery.capacity - house.maxoutput  
                            # print(battery.capacity)
                            
                
                print(battery.capacity)
                            # unused_houses.remove(house)

                # else:
                    # battery.remove_house(house)
                    # print(battery.capacity)
                    # print("pastte niet")
                    # unused_houses.append(house)


                # if battery.capacity < 0:
                #     battery.houses_to_battery.remove(house)
                #     unused_houses.append(house)
                print(battery.capacity)        

                # if it is a new coordinate add to dictionary with right connected battery and add to cables_Coordinates
                #             
for battery in batteries:
    count_houses = count_houses + len(battery.houses_to_battery)

# print output, house id, coordinates and coordinates of closest item
print(f"id: {house.id}")
print(f"house: ({house.x}, {house.y})")
print(f"closest_connection: {closest_connection}")


# cable costs calculation, calculate costs for all grid segments, so its min start point battery
number_of_cables = int(len(cables_coordinates))
costs_all_cables = (number_of_cables * 9) - len(batteries)*9
print(f"costs all cables: {costs_all_cables}")

count_houses = 0
for battery in batteries:
    count_houses = count_houses + len(battery.houses_to_battery)
print(f"number of houses connected: {count_houses}")    

ax = plt.subplot(111)

for battery in batteries:
    batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')
for house in houses:
    houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
    plt.plot(*zip(*house.cables), color='k')
plt.savefig("sofietest.png")