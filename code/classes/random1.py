import load_data
import house
import battery
import random

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

# load data 
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# variable for calculation and creating dictionary
own_costs = 0
dict= {}

capaciteit = 1507.00

# print houses and batteries
house_locs_x = []
house_locs_y = []

battery_locs_x = []
battery_locs_y = []

# loop to link all batteries
for battery in batteries:

    battery_locs_x.append(int(battery.x))
    battery_locs_y.append(int(battery.y))

for house in houses:

    house_locs_x.append(int(house.x))
    house_locs_y.append(int(house.y))

    rand_battery = random.choice(batteries)

    if rand_battery.capaciteit < house.maxoutput:
        while battery.capaciteit <= house.maxoutput:
            rand_battery = random.choice(batteries)

    else:
        rand_battery.capaciteit = rand_battery.capaciteit - house.maxoutput
    
    house_x = int(house.x) 
    house_y = int(house.y)

    battery_x = int(rand_battery.x) 
    battery_y = int(rand_battery.y)

    cutting_point_x = house.x 
    cutting_point_y = rand_battery.y


    #plot line between house and cutting point 
    x = [house_x, cutting_point_x, battery_x]
    y = [house_y, cutting_point_y, battery_y]

    xt = abs(house_x - battery_x)
    yt = abs(house_y - battery_y)
    dis = xt + yt
    price = dis * 9 
    own_costs = own_costs + price
    dict[house.id] = price

    ax = plt.subplot(111)

    houses_plt = ax.scatter(house_locs_x, house_locs_y, color='k', marker='*')
    batteries_plt = ax.scatter(battery_locs_x, battery_locs_y, color='r', marker='^')

    plt.plot(x,y)
    
    if 

    # print(own_costs)
for battery in batteries:
    print(battery.id)
    print(battery.capaciteit)

plt.savefig("randomplot.png")

# print(dict)
# print(own_costs)