import load_data
import house
import battery
from pprint import pprint

import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style

reader = load_data.Load_data()

batteries = reader.load_batteries()

houses = reader.load_houses()

battery_locs_x = []
battery_locs_y = []

house_locs_x = []
house_locs_y = []

for battery in batteries:
    battery_locs_x.append(battery.x)
    battery_locs_y.append(battery.y)


for house in houses:
    house_locs_x.append(house.x)
    house_locs_y.append(house.y)
    


fig = plt.figure()
ax1 = plt.subplot(111)

batteries = ax1.scatter(battery_locs_x, battery_locs_y, color='r')
houses = ax1.scatter(house_locs_x, house_locs_y, color='b')

ax1.set(xlabel='x-axis', ylabel='y-axis',
      title='District 1')
ax1.legend([houses, batteries], ['Houses','Batteries'], loc=3)
fig.savefig("test.pdf")

