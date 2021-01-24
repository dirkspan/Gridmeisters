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

# initialize houses count
count_houses = 0


# first add the batteries as connect option and add as first items in dictionary
for battery in batteries:
    cables_coordinates.append(battery.coordinates)
        
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
    
     # if there is already a connection for this house
    if house.coordinates == connection:
        battery.connect_house(house)
        print("verbind2")

    # loops through dictionary and cables, to compare
    for cable_point in house.cables:
            
        # find connection point in dictionary 
        if cable_point == connection:
                
            # connect battery
            battery.connect_house(house)

            # waar dit niet staat gaat het dus fout....
            print("verbonden4")

    # if it is a new coordinate add to dictionary with right connected battery and add to cables_Coordinates
    for tuple in house.cables:
        if tuple not in cables_coordinates:
            cables_coordinates.append(tuple)


            
# print output, house id, coordinates and coordinates of closest item
    print(f"id: {house.id}")
    print(f"house: ({house.x}, {house.y})")
    print(f"closest_connection: {closest_connection}")


# cable costs calculation, calculate costs for all grid segments, so its min start point battery
number_of_cables = int(len(cables_coordinates))
costs_all_cables = (number_of_cables * 9) - len(batteries)*9
print(f"costs all cables: {costs_all_cables}")


for battery in batteries:
    count_houses = count_houses + len(battery.houses_to_battery)
    print(f"number of houses to {battery.id} : {len(battery.houses_to_battery)}")
print(f"number of houses connected: {count_houses}")    


ax = plt.subplot(111)

for battery in batteries:
    batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')
for house in houses:
    houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
    plt.plot(*zip(*house.cables), color='k')
plt.savefig("testshared.png")