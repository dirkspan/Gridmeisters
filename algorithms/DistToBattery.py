import models.battery
import models.cables
import models.house
import models.load_data
from . import helper
import random
import matplotlib.pyplot as plt
from matplotlib import style

# read in all data
reader = models.load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

def first_algorithm():
    """
    Connects each house to the closest battery based on distance 
    and uses the hillclimber algorithm to find the optimal solution.
    """
   
    # houses that are currently not being used because the battery is full
    unused_houses = []


    # random shuffle all houses
    random.shuffle(houses)

    for house in houses:

        # keeps track of distances between each house and battery
        dist_dict = {}

        # keeps track on wether battery has sufficient capacity
        keep_track = []

        for battery in batteries:
           
            # battery has sufficient capacity
            if battery.status(house) == True:

                # calculate distance between house and battery
                distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

                # stores distance in dictionary
                dist_dict[battery] = distance

                keep_track.append(1)

            else:
                keep_track.append(0)

        # full battery move on to the next one
        if keep_track.count(1) == 0:
            unused_houses.append(house)

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
            # house_costs = house.add_costs(battery)
            battery.add_house_info(house)
            house.route_calc(battery)
            

            # no unused houses left, applies hillclimber to optimalize connections
            if len(unused_houses) == 0:
                helper.hillclimber(batteries, houses)

    # total costs for the cables
    total_costs = 0

    # for battery in batteries:
    #     cables_coordinates = []
    #     for house in battery.houses_to_battery:
    #         for cable in house.cables:
    #             if cable not in cables_coordinates:
    #                 cables_coordinates.append(cable.cable_x, cable.cable.y)
    #     print(cables_coordinates)
            # for tuple in house.cables:
            #     print(tuple)
            #     if tuple not in cables_coordinates:
            #         print(f"new: {tuple}")
                    # print(cables_coordinates)
                    # cables_coordinates.append(tuple)
        
        # for j in cables_coordinates:
        #     print(j)

        # print(cables_coordinates)
        # # print(cables_coordinates)

        # number_of_cables = len(cables_coordinates) - 1
        # print(number_of_cables)
        # costs_battery = number_of_cables * 9 + 5000
        # total_costs = total_costs + costs_battery

    return total_costs


def plot_first_algorithm():
    """
    Plots the cables, houses and batteries for the Hillclimber algorithm
    """
    
    i = -1

    for battery in batteries:
        i += 1
    
        for house in battery.houses_to_battery:

            colors = ['c', 'k', 'b', 'g', 'r']

            cutt_point_x = house.x
            cutt_point_y = battery.y

            x = [house.x, cutt_point_x, battery.x]
            y = [house.y, cutt_point_y, battery.y]

            plt.plot(x,y, color= colors[i])

            ax = plt.subplot()

            houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
            batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

    fig = plt.savefig("hillclimberfigure.png")
    return fig
 
def run_output():

    for curr_batt in batteries:
        print(curr_batt)

        for curr_house in curr_batt.houses_to_battery:
            print(curr_house)

            for cable_point in curr_house.cables:
                print(cable_point)