import algorithms.DistToBattery
import algorithms.Random
import algorithms.ConstraintRelaxation
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
    print("Please select an algorithm to run: 1 = Randomize, 2 = HillClimber and 3 = Constraint relaxation 4 = Multiple times algorithm 3 5 = Multiple times algorithm 4 ")
    print("Please be aware that the first two algorithms both have overlapping cables")

    algo_choice = input("Make a choice: ")

    yes = 'Y' or 'y' or 'yes'

    if algo_choice == '1':
        print(f"The total costs for this district are: {algorithms.Random.random_algorithm()}")
        plot_choice = input("Do you like to see the visualization and output? ,Y/N: ")
        if plot_choice == yes:
            algorithms.Random.plot_random_algorithm()
            algorithms.Random.run_rand_output()

    elif algo_choice == '2':

        print(f"The total costs for this district are: {algorithms.DistToBattery.first_algorithm()}")

        plot_choice = input("Do you like to see the visualization and output?, Y/N: ")

        if plot_choice == yes:
            algorithms.DistToBattery.plot_first_algorithm()
            algorithms.DistToBattery.run_output()

    elif algo_choice == '3':

        algorithms.ConstraintRelaxation.optimum_creating()
        
    elif algo_choice == '5':
        algorithms.DistToBattery.run_multiple_times()
    
    elif algo_choice == '6':
        algorithms.ConstraintRelexation.run_multiple_times()
  
  
    elif algo_choice not in ['1', '2', '3', '4']:
        print("Please make a choice between 1 and 5")
