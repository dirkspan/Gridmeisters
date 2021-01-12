import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import csv

battery_list = []
house_list = []
lijst_bat1 = []

with open('data/district_1/district-1_batteries.csv', 'r') as battery_data:
    battery_reader = csv.DictReader(battery_data)
    for row in battery_reader:
        battery_list.append(row)

with open('data/district_1/district-1_houses.csv', 'r') as houses_data:
    houses_reader = csv.DictReader(houses_data)
    for row in houses_reader:
        house_list.append(row)

for i in house_list:
    xh = int(i['x'])
    yh = int(i['y'])
    id = int(i['id'])

    #prints the id of the current house
    print(id)

    dict = {}

    for i in battery_list:
        id = i['id']

        xb = int(i['x'])
        yb = int(i['y'])

        xt = abs(xh - xb)
        yt = abs(yh - yb)
        dis = xt + yt

        dict[id] = dis

    nearest_bat = min(dict.items(), key=lambda x:x[1])
   
    # prints the id of the nearest battery
    print (nearest_bat[0])

    









