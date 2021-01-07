import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

houses = pd.read_csv('district-3_houses.csv')
batteries = pd.read_csv('district-3_batteries.csv')

fig = plt.figure()
ax1 = plt.subplot(111)
houses = ax1.scatter(houses.x, houses.y, color='k')
batteries = ax1.scatter(batteries.x, batteries.y, color='r')
ax1.set(xlabel='x-axis', ylabel='y-axis',
      title='District 3')
ax1.legend([houses, batteries], ['Houses','Batteries'], loc=3)
fig.savefig("District3.pdf")


# a = batteries.pop('capaciteit')
# b = houses.pop('maxoutput')