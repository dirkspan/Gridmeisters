import models.battery
import models.cables
import models.house
import models.load_data
from . import helper
from . import Hillclimber
import random
import matplotlib.pyplot as plt
from matplotlib import style

# read in all data
reader = models.load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

def optimum_creating():
    """
    Connects each house to the closest battery based on distance
    """
    random.shuffle(houses)

    # houses that are currently not being used because the battery is full
    unused_houses = []

    # total costs for the cables
    total_costs = 0

    # loop to connect all houses
    for house in houses:

        # keeps track of distances between each house and battery
        dist_dict = {}

        # keeps track on wether battery has sufficient capacity
        keep_track = []

        # loop to check the distance to all batteries
        for battery in batteries:

            # battery has sufficient capacity
            if battery.status(house) == True:

                # calculate distance between house and battery
                distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

                # stores distance in dictionary
                dist_dict[battery] = distance

                # saves if house is connected or not
                keep_track.append(1)

            else:
                # saves if house is connected or not
                keep_track.append(0)

        # full battery move on to the next one
        if keep_track.count(1) == 0:
            unused_houses.append(house)

        # if battery is not full
        else:

            # return closest distance of a house to the battery
            closest_distance = min(dist_dict.items(), key=lambda x: x[1])
            closest_battery= closest_distance[0]
            battery = closest_battery

            # define cutting point between battery and house
            route = (house.x, battery.y)

            # connects house to battery and vice versa
            house.connect_to_battery(battery)
            battery.connect_house(house)

            # adds costs of cables for this house to the battery
            # house.add_costs(battery)
            # battery.add_house_info(house)
            
            # no unused houses left, applies hillclimber to optimalize connections
            if len(unused_houses) <= 1:

                # update weird outlayers to closest battery
                helper.hillclimber(batteries, houses)

    # if algorithm is finished run constraint_relaxation algorithm
    if len(unused_houses) <= 1:
        constraint_relaxation()

        # run_output()
        total_costs = constraint_relaxation()
    
    return total_costs
    




def constraint_relaxation():

    """
    Connects cables of coupled houses in most profitable way, closest option to connect
    """
    

    # initialize total costs as 0 
    total_costs = 0

    # initializing to help printing 
    i = -1

    # loop through all batteries, to improve all 5 routes
    for battery in batteries:

        # for every battery append to costs for this battery, costs for each battery are 5000 in this case
        costs_of_battery = 5000
        total_costs += costs_of_battery
        i += 1

        # initialize empty list for cable coordinates of this battery and start with coordinates battery
        cables_coordinates = []
        cables_coordinates.append(battery.coordinates)

        # for all houses connected to current battery
        for house in battery.houses_to_battery:

            # initalize an empty list, for all options for this battery
            connect_options = []

            # initialize dictionary to save distance
            dist_dict = {}

            #  for all cables connected to battery, calculate distance to current house
            for cable_point in cables_coordinates:
                distance = int(abs(house.coordinates[0] - cable_point[0]) + abs(house.coordinates[1] - cable_point[1]))
                connect_options.append(distance)
                dist_dict[cable_point] = distance

            # identify closest distance as place to connect this house
            closest_distance = min(dist_dict.items(), key=lambda x: x[1])
            closest_connection = closest_distance[0]
            connection = closest_connection

            # run function to make the route
            house.shortest_route(connection, house)
            
            # update cables_coordinates with all new coordinates
            for cable in house.cables:
                if cable not in cables_coordinates:
                    cables_coordinates.append(cable)
            
            # make plot of this algorithm
            colors = ['c', 'k', 'b', 'g', 'r']

            # cutting point is the corner to the connection point
            cutt_point_x = house.x
            cutt_point_y = connection[1]

            # plot from house to connection point
            x = [house.x, cutt_point_x, connection[0]]
            y = [house.y, cutt_point_y, connection[1]]

            # plot all houses, batteries and lines
            plt.plot(x,y, color= colors[i])
            ax = plt.subplot(111)
            houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
            batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

        # calculate costs for all cables to this battery and add this to the total costs
        number_of_cables = len(cables_coordinates)
        costs_of_cable = 9
        cables_costs = number_of_cables * costs_of_cable
        total_costs = total_costs + cables_costs
    
        # make plot
        plt.savefig("Constraintrelaxation.png")

    return total_costs
        

def run_output():
    """
    Runs output
    """

    for curr_batt in batteries:
        print(curr_batt)

        for curr_house in curr_batt.houses_to_battery:
            print(curr_house)

            for cable_point in curr_house.cables:
                print(cable_point)


def run_multiple_times():

    results = []
    
    curr_total_costs = 50000
    
    for i in range(1000):
        optimum_creating()
        new_total_costs = constraint_relaxation()

        if new_total_costs < curr_total_costs:
            curr_total_costs = new_total_costs
        results.append(curr_total_costs)
        print(curr_total_costs)
        print(results)
    
        for house in houses:
            house.clear_house()
        for battery in batteries:
            battery.clear(house)
