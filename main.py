import algorithms.DistToBattery
import algorithms.Random
import algorithms.helper
from data import *
import models.battery
import models.cables
import models.house
from models.load_data import Load_data
import csv
import os
from sys import argv




if len(argv) < 3:
    print("Type in the correct files, f.e: python3 main.py data/dist1_b.csv data/dist1_h.csv")
    exit()
else:
    # # dit is hillclimber algoritme
    # print(f"The total costs for this district are: {algorithms.DistToBattery.first_algorithm()}\nThe figure will be saved in the directory look for figure.png")
    # algorithms.DistToBattery.plot_first_algorithm()
    # # algorithms.DistToBattery.run_output()

    # dit is AlgoritmeTwee, comment het uit om te runnen
    print(f"The total costs for this district are: {algorithms.AlgoritmeTwee.second_algorithm()}\nThe figure will be saved in the directory look for figure2.png")
    algorithms.AlgoritmeTwee.plot_second_algorithm()
    algorithms.AlgoritmeTwee.run_sec_output

    # dit is random algoritme, comment het uit om te runnen
    # algorithms.Random.random_algorithm()
    # algorithms.Random.plot_random_algorithm()