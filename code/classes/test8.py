import cables
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

house = houses[4]
battery = batteries[0]

reader1= cables.Cable()
cables= reader1.coordinates_cables(house, battery)

for cable in cables:
    print(cable)

