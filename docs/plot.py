import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

# data inlezen
houses = pd.read_csv('district-3_houses.csv')
batteries = pd.read_csv('district-3_batteries.csv')

# figuur plotten
fig = plt.figure()
ax = plt.subplot(111)

# x,y = scatter
houses = ax.scatter(houses.x, houses.y, color='k')
batteries = ax.scatter(batteries.x, batteries.y, color='r')
ax.set(xlabel='x-axis', ylabel='y-axis',
      title='District 3')

# legenda
ax.legend([houses, batteries], ['Houses','Batteries'], loc=3)

# figuur opslaan
fig.savefig("District3.pdf")


# a = batteries.pop('capaciteit')
# b = houses.pop('maxoutput')
