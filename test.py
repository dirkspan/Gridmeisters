import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import csv

# houses = pd.DataFrame(columns=['id','x','y','capaciteit'])

# data = pd.read_csv('district-1_batteries.csv')

# # print(data)

# new_data = houses.append(data)
# print(new_data)

battery_list = []
house_list = []

with open('data/district_1/district-1_batteries.csv', 'r') as battery_data:
    battery_reader = csv.DictReader(battery_data)
    for row in battery_reader:
        battery_list.append(row)

with open('data/district_1/district-1_houses.csv', 'r') as houses_data:
    houses_reader = csv.DictReader(houses_data)
    for row in houses_reader:
        house_list.append(row)


total_distance = []
dict = {}


for i in house_list:
    xh = int(i['x'])
    yh = int(i['y'])
    id = int(i['id'])
    # print(id)

    total_distance = []
    unieke_id = []
    minimaallist = []
    for i in battery_list:
        id = i['id']
        xb = int(i['x'])
        yb = int(i['y'])
        unieke_id.append(id)

        xt = abs(xh - xb)
        yt = abs(yh - yb)
        dis = xt + yt
       
        total_distance.append(dis)


    minimaal = min(total_distance)
    minimaallist.append(minimaal)

print(minimaallist)    
    



   











