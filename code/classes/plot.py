import load_data


import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style


batteries = load_data.Load_data.load_batteries
houses = load_data.Load_data.load_houses

print(houses)



# import numpy as np
# import pandas as pd


# houses = pd.read_csv('data/district_1/district-1_houses.csv')
# batteries = pd.read_csv('data/district_1/district-1_batteries.csv')

# houses1 = houses.sample(n=30)
# houses2 = houses.sample(n=30)
# houses3 = houses.sample(n=30)
# houses4 = houses.sample(n=30)
# houses5 = houses.sample(n=30)


# fig = plt.figure()
# ax1 = plt.subplot(111)


# batteries = ax1.scatter(batteries.x, batteries.y, color='r')
# houses1 = ax1.scatter(houses1.x, houses1.y, color='b')
# houses2 = ax1.scatter(houses2.x, houses2.y, color='m')
# houses3 = ax1.scatter(houses3.x, houses3.y, color='k')
# houses4 = ax1.scatter(houses4.x, houses4.y, color='c')
# houses5 = ax1.scatter(houses5.x, houses5.y, color='g')

# ax1.set(xlabel='x-axis', ylabel='y-axis',
#       title='District 1')
# ax1.legend([houses, batteries], ['Houses','Batteries'], loc=3)
# fig.savefig("test.pdf")

