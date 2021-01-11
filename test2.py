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

# minlen = {}




# for i in house_list:
i = house_list[0]

xh = int(i['x'])
yh = int(i['y'])

id = int(i['id'])
# print(id)

dict = {}

i = battery_list[1]
# for i in battery_list:
# id = i['id']

xb = int(i['x'])
yb = int(i['y'])

xt = xh - xb
print('x coordinaten: h,b,t')
print(xh)
print(xb)
print(xt)

verschil = int(xt)
print(verschil)

xhuidig = xh

for i in verschil:
    xhuidig = xhuidig - 1
    print (xhuidig)

yt = abs(yh - yb)
dis = xt + yt
# print(dis)

dict[id] = dis

# nearest_bat = min(dict.items(), key=lambda x:x[1])  
   
# print (nearest_bat)



