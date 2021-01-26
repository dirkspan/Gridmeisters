import algorithms.DistToBattery
import algorithms.Random
import algorithms.ConstraintRelexation
import algorithms.Random_ConstraintRelaxation
import algorithms.helper
import algorithms.AlgoritmeTwee
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
    print("Please select an algorithm to run: 1 = Randomize, 2 = HillClimber, 3 = Constraint relaxation, 4 = Random with constraint relaxation")
    print("Please be aware that the first two algorithms both have overlapping cables")

    algo_choice = input("Make a choice: ")
    if algo_choice == '4':
        algorithms.DistToBattery.run_multiple_times()
  

    if algo_choice == '0':

        algorithms.DistToBattery.shared_costs()


    if algo_choice == '1':
        print(algorithms.Random.random_algorithm())
        plot_choice = input("Do you like to see the visualization and output? ,Y/N: ")
        if plot_choice == 'Y':
            algorithms.Random.plot_random_algorithm()
            algorithms.Random.run_rand_output()

    elif algo_choice == '2':

        print(f"The total costs for this district are: {algorithms.DistToBattery.first_algorithm()}")

        plot_choice = input("Do you like to see the visualization and output?, Y/N: ")

        if plot_choice == 'Y':
            algorithms.DistToBattery.plot_first_algorithm()
            algorithms.DistToBattery.run_output()

    elif algo_choice == '3':
        algorithms.ConstraintRelexation.optimum_creating()

    elif algo_choice == '4':
        algorithms.Random_ConstraintRelaxation.constraint_random()
        

    elif algo_choice not in ['1', '2', '3', '4']:
        print("Please make a choice between 1, 2, 3 or 4")
