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

def random_algorithm():
    """
    Connects each house randomly to a battery
    """

    count = 0

    tot_rand_costs = 0

    random.shuffle(houses)

    for battery in batteries:

        for house in houses:

            if battery.status(house) == True and house.connected_to == None:

                battery.connect_house(house)
                house.route_calc(battery)
                house.add_costs(battery)
                tot_rand_costs += house.costs

                house.connect_to_battery(battery)
                count += 1

    if count < 149:
        battery.clear(house)
        house.clear_house()
        random_algorithm()
    else:
        return tot_rand_costs 


def plot_random_algorithm():
    """
    Plots the cables, houses and batteries for the Random algorithm
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

    fig = plt.savefig("randomfigure.png")
    return fig

def run_rand_output():

    for curr_batt in batteries:
        print(curr_batt)

        for curr_house in curr_batt.houses_to_battery:
            print(curr_house)

            for cable_point in curr_house.cables:
                print(cable_point)
