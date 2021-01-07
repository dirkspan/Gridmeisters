# import csv
# from .battery import *
# from .house import *

# class Graph():

#     def __init__(self, dict):
#         pass
#         self.house_list = []
#         self.battery_list = []

#     def load_batteries(self, battery_data):

#         with open('district-1_batteries.csv', 'r') as battery_data:
#         battery_reader = csv.DictReader(battery_data)
#             for row in battery_reader:

#                 id = int(row['id'])
#                 battery = Battery(int(row['id']), row['x'], row['y'], row['capaciteit'])

#                 # dict[id] = battery
                

#     def load_houses(self, house_data):

#         with open('district-1_batteries.csv', 'r') as house_data:
#         house_reader = csv.DictReader(house_data)
#             for row in house_reader:

#                 # id = int(row['id'])
#                 house = House(int(row['id']) row['x'], row['y'], row['maxoutput'])
#                 self.house_list.append(house)    



import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import random

houses = pd.read_csv('district-3_houses.csv')
batteries = pd.read_csv('district-3_batteries.csv')

a = houses.sample()

print(houses)

print(a)

fig = plt.figure()
ax1 = plt.subplot(111)

a = ax1.scatter(a.x, a.y, color='m')

houses = ax1.scatter(houses.x, houses.y, color='k')
batteries = ax1.scatter(batteries.x, batteries.y, color='r')

ax1.set(xlabel='x-axis', ylabel='y-axis',

title='District 3')

ax1.legend([houses, batteries], ['Houses','Batteries'], loc=3)
fig.savefig("Districtblabla.pdf")