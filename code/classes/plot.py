import load_data
import house
import battery
from pprint import pprint

import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy

from bokeh.plotting import figure, show

reader = load_data.Load_data()

batteries = reader.load_batteries()

houses = reader.load_houses()

battery_locs_x = []
battery_locs_y = []

house_locs_x = []
house_locs_y = []

for battery in batteries:
    battery_locs_x.append(int(battery.x))
    battery_locs_y.append(int(battery.y))


for house in houses:
    house_locs_x.append(int(house.x))
    house_locs_y.append(int(house.y))

# df = pd.DataFrame(columns=list('xy'))

# for house in houses:
#     df = df.append({'x': house.x, 'y': house.y}, ignore_index=True)
# print(df)   

fig = plt.figure()
ax1 = plt.subplot(111)

houses = ax1.scatter(house_locs_x, house_locs_y, color='k', marker='*')
batteries = ax1.scatter(battery_locs_x, battery_locs_y, color='r', marker='^')

ax1.set(xlabel='x-axis', ylabel='y-axis',
      title='District 1')
ax1.legend([houses, batteries], ['Houses','Batteries'], loc=3)
fig.savefig("test4.pdf")

