import models.battery
import models.cables
import models.house
import models.load_data
from . import helper
import random
import matplotlib.pyplot as plt
from matplotlib import style
import copy

# read in all data
reader = models.load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

def random_algorithm():
    """
    Connects each house randomly to a battery
    """

    count = 0
    battery_price = 5000
    tot_rand_costs = 5 * battery_price
    temp_houses = copy.deepcopy(houses)
    random.shuffle(temp_houses)

    for battery in batteries:
        house_list = []
        

        for i in range(30):

            house = random.choice(temp_houses)

            temp_houses.remove(house)

            battery.connect_house(house)
            house.route_calc(battery)
            house.add_costs(battery)
            tot_rand_costs = tot_rand_costs + house.costs
            
            house.connect_to_battery(battery)

            house_list.append(house.id)

            if battery.capacity < 0:
                battery.remove_house(house)
                battery.connect_house(random.choice(houses))


    return tot_rand_costs 
    

    # print(f"kosten!:{tot_rand_costs}")


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


def run_multiple_times():

    results = []
    x = 0
    curr_total_costs = 100000
    count = 0
    for i in range(100000):
        x += 1
        print(x)
        # new_total_costs = random_algorithm()
        count += random_algorithm()
        # if new_total_costs < curr_total_costs:
            # curr_total_costs = new_total_costs

        # results.append(curr_total_costs)
        # print(curr_total_costs)
        # print(results)
        # print(len(results))

        for house in houses:
            house.clear_house()
            for battery in batteries:
                battery.clear(house)
    
    average = count/100000
    print (average)
    print (count)
    
        
        
