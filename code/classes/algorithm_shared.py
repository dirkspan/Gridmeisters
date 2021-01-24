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

# introduce battery dictionary 
bat_dict = {}

# initialize houses count
count_houses = 0

# first add the batteries as connect option and add as first items in dictionary
for battery in batteries:
    bat_dict[battery.coordinates] = battery.id
    cables_coordinates.append(battery.coordinates)
        
# loop for house in houses
for house in houses:
    # check if all houses are looped
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
    
    # start is house, end is connection coordinates
    current_x = house.x
    end_x= connection[0]
    current_y = house.y
    end_y = connection [1]
    
    # only if house isn't already connected, append first coordinate
    if house.coordinates != connection: 
        house.cables.append((current_x, current_y))

    # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
    if current_y < end_y:
        while current_y < end_y:
            current_y += 1
            house.cables.append((current_x, current_y))
    elif current_y > end_y:
        while current_y > end_y:
            current_y -= 1
            house.cables.append((current_x, current_y))
    if current_x < end_x:
        while current_x < end_x:
            current_x += 1
            house.cables.append((current_x, current_y))
    elif current_x > end_x:
        while current_x > end_x:
            current_x -= 1
            house.cables.append((current_x, current_y))
   
    # dictionary with battery coupeled.
    for battery in batteries:
        if connection == battery.coordinates:
            battery.connect_house(house)
            for cable_point in cables_coordinates:

                # if cable point not in list yet, append to dictionary with coupeled battery
                if cable_point not in cables_coordinates:
                    house.connect_to = battery.id
                    bat_dict[cable_point] = house.connected_to
    
    # loops through dictionary and cables, to compare
    for item in bat_dict:
        for cable_point in house.cables:
            
            # if there is already a connection for this house
            if house.coordinates == connection:
                battery.connect_house(house)
                batitem = bat_dict.get(item)

                # add same connected battery as connectedbattery of connected grid piece
                house.connected_to = batitem

            # find connection point in dictionary 
            if cable_point == item:
                
                # connect battery
                battery.connect_house(house)

                # waar dit niet staat gaat het dus fout....
                print("verbonden4")
            

                # get coupeled id of this cable grid
                batitem = bat_dict.get(item)

                # add same connected battery as connectedbattery of connected grid piece
                house.connected_to = batitem
                print(f"connected to {house.connected_to}")
                
                # capacity of battery
                print(battery.capacity)
                battery.capacity = battery.capacity - house.maxoutput  
                print(battery.capacity)
                        
           

    # if it is a new coordinate add to dictionary with right connected battery and add to cables_Coordinates
    for tuple in house.cables:
        if tuple not in cables_coordinates:
            cables_coordinates.append(tuple)
            if tuple not in bat_dict:   
                    batitem = bat_dict.get(item)
                    house.connected_to = batitem
                    bat_dict[tuple] = house.connected_to


# print output, house id, coordinates and coordinates of closest item
    print(f"id: {house.id}")
    print(f"house: ({house.x}, {house.y})")
    print(f"closest_connection: {closest_connection}")

print(bat_dict)

# cable costs calculation, calculate costs for all grid segments, so its min start point battery
number_of_cables = int(len(cables_coordinates))
costs_all_cables = (number_of_cables * 9) - len(batteries)*9
print(f"costs all cables: {costs_all_cables}")


for battery in batteries:
    count_houses = count_houses + len(battery.houses_to_battery)
print(f"number of houses connected: {count_houses}")    


ax = plt.subplot(111)

for battery in batteries:
    batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')
for house in houses:
    houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
    plt.plot(*zip(*house.cables), color='k')
plt.savefig("testshared.png")