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


def second_algorithm():
    """
    Schrijf hier je code voor tweede algoritme, je hoeft niks te printen
    of returnen, zorg er alleen voor dat de huizen geappend worden aan alle batterijen
    """
    pass


def second_algorithm_plot():
    """
    Hier kan je tweede algoritme plotten
    """
    pass
    # i = -1

    # for battery in batteries:
    #     i += 1
    
    #     for house in battery.houses_to_battery:

    #         colors = ['c', 'k', 'b', 'g', 'r']

    #         cutt_point_x = house.x
    #         cutt_point_y = battery.y

    #         x = [house.x, cutt_point_x, battery.x]
    #         y = [house.y, cutt_point_y, battery.y]

    #         plt.plot(x,y, color= colors[i])

    #         ax = plt.subplot()

    #         houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
    #         batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

    #         fig = plt.savefig("2ndplot.png")
    # return fig
     

def run_sec_output():

    """
    Hier run je output, print dus per regel batterij etc...
    """
    pass     