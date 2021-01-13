import load_data
import house
import battery
# import cables
import random

from pprint import pprint
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import array 




reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()


# reader1 = cables.Grid()
# reader2 = cables.Grid()
# house_x_dist = reader1.cables(houses, batteries)
# house_y_dist = reader2.cables(houses, batteries)

# print(house_x_dist)
# print(house_y_dist)



import random

house_locs_x = []
house_locs_y = []

battery_locs_x = []
battery_locs_y = []

for battery in batteries:

    battery_locs_x.append(int(battery.x))
    battery_locs_y.append(int(battery.y))

for house in houses:

    house_locs_x.append(int(house.x))
    house_locs_y.append(int(house.y))

    rand_battery = random.choice(batteries)

    house_x = house.x 
    house_y = house.y

    battery_x = rand_battery.x 
    battery_y = rand_battery.y

    cutting_point_x = house.x 
    cutting_point_y = rand_battery.y


    #plot line between house and cutting point 
    x = [house_x, cutting_point_x, battery_x]
    y = [house_y, cutting_point_y, battery_y]

    ax = plt.subplot(111)

    houses_plt = ax.scatter(house_locs_x, house_locs_y, color='k', marker='*')
    batteries_plt = ax.scatter(battery_locs_x, battery_locs_y, color='r', marker='^')

    plt.plot(x,y)
    plt.savefig("doehetnou.png")







# df = pd.DataFrame(columns=list('xy'))

# for house in houses:
#     df = df.append({'x': house.x, 'y': house.y}, ignore_index=True)
# print(df)   

# battery_locs_x = []
# battery_locs_y = []

# house_locs_x = []
# house_locs_y = []

# for battery in batteries:
#     battery_locs_x.append(int(battery.x))
#     battery_locs_y.append(int(battery.y))

# for house in houses:
#     house_locs_x.append(int(house.x))
#     house_locs_y.append(int(house.y))

# fig = plt.figure()
# ax1 = plt.subplot(111)

# houses = ax1.scatter(house_locs_x, house_locs_y, color='k', marker='*')
# batteries = ax1.scatter(battery_locs_x, battery_locs_y, color='r', marker='^')
# step = plt.step(battery_locs_x, house_locs_y)

# ax1.set(xlabel='x-axis', ylabel='y-axis',
#       title='District 1')
# ax1.legend([houses, batteries], ['Houses','Batteries'], loc=3)
# fig.savefig("test1.pdf")
