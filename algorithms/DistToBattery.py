import models.battery
import models.cables
import models.house
import models.load_data
from . import helper
import random
import matplotlib.pyplot as plt
from matplotlib import style

import copy
from copy import deepcopy

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

    # total costs for the cables
    total_costs = 0

    random.shuffle(houses)
    
    for house in houses:

        # keeps track of distances between each house and battery
        dist_dict = {}

        # keeps track on wether battery has sufficient capacity
        keep_track = []

        for battery in batteries:

            # costs for all cables connected to the current battery
            battery_costs = 0

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
            house.add_costs(battery)
            house.route_calc(battery)
            total_costs += house.costs

            # no unused houses left, applies hillclimber to optimalize connections
            if len(unused_houses) == 0:
                helper.hillclimber(batteries, houses)   

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

            houses_plt = ax.scatter(house.x, house.y, color='k', marker='p')
            batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

    fig = plt.savefig("DistTobattery.png")
    return fig
 
def run_output():

    for curr_batt in batteries:
        print(curr_batt)

        for curr_house in curr_batt.houses_to_battery:
            print(curr_house)

            for cable_point in curr_house.cables:
                print(cable_point)

def run_multiple():

    curr = copy.deepcopy(first_algorithm())
    print(curr)

    new = first_algorithm()
    print(new)


def shared_costs():

    first_algorithm()

    count = 0

    x = [1, 2, 5, 7]
    y = [0, 2, 3, 5]

    shared_cables = []

    for house in houses:

        for cable in house.cables:
            print(cable)
            # x.append(cable.cable_x)
            # y.append(cable.cable_y)
            # if cable.cable_x in x and cable.cable_y in y:
            #     count += 1
            #     shared_cables.append(cable.cable_x)
            #     print('ok')
            #     shared_cables.append(cable.cable_y)
        

    # print(count)
    # print(shared_cables)
          

def run_multiple_times():

    results = []
    
    curr_total_costs = 50000
    
    for i in range(1000):
        
        new_total_costs = first_algorithm()
        
        if new_total_costs < curr_total_costs:
            curr_total_costs = new_total_costs

            results.append(int(curr_total_costs))
            print(curr_total_costs)
            print(results)
            plot_first_algorithm()


        for house in houses:
            house.clear_house()
            for battery in batteries:
                battery.clear(house)
        

    # print(count)
    # print(shared_cables)
          

