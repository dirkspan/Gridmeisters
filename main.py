import algorithms.Hillclimber
import algorithms.Random
import algorithms.ConstraintRelaxation
import algorithms.helper
from data import *
import models.battery
import models.cables
import models.house
from models.load_data import Load_data
from sys import argv


if len(argv) < 3:
    print("Type in the correct files, f.e: python3 main.py data/dist1_b.csv data/dist1_h.csv")
    exit()
else:
    print(f"Please select an algorithm to run:1 = Randomize\n2 = HillClimber\n3 = Constraint relaxation")
    print("Please be aware that the first two algorithms both have overlapping cables")

    algo_choice = input("Please make a choice: between 1, 2 and 3 ")

    if algo_choice == '1':
        print(f"The total costs for this district are: {algorithms.Random.random_algorithm()}")
        plot_choice = input("Do you like to see the visualization and output? ,Y/N: ")
        if plot_choice == 'Y' or 'y' or 'yes' or 'Yes':
            algorithms.Random.plot_random_algorithm()
            algorithms.Random.run_rand_output()      

            multiple_choice = input("Would you like to run this algorithm multiple times to get the optimal result? Y/N ")
            if multiple_choice == 'Y' or 'y' or 'yes' or 'Yes':
                algorithms.Random.run_multiple_times()
            else:
                print('Okay ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ') 
                exit()

    elif algo_choice == '2':
        algorithms.Hillclimber.first_algorithm()
        print(f"The total costs for this district are: {algorithms.Hillclimber.calc_total_cost()}")

        plot_choice = input("Do you like to see the visualization and output?, Y/N: ")
    
        if plot_choice == 'Y' or 'y' or 'yes' or 'Yes':
            algorithms.Hillclimber.plot_first_algorithm()
            algorithms.Hillclimber.run_output()

            multiple_choice = input("Would you like to run this algorithm multiple times to get the optimal result? Y/N ")
            if multiple_choice == 'Y' or 'y' or 'yes' or 'Yes':
                algorithms.Hillclimber.run_multiple_times()
            else:
                print('Okay ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ') 
                exit()   

    elif algo_choice == '3':
        algorithms.ConstraintRelaxation.optimum_creating()

        plot_choice = input("Do you like to see the visualization and output?, Y/N: ")

        if plot_choice == 'Y' or 'y' or 'Yes' or 'yes':
            algorithms.ConstraintRelaxation.constraint_relaxation()
            algorithms.ConstraintRelaxation.run_output()
            
            multiple_choice = input("Would you like to run this algorithm multiple times to get the optimal result? Y/N")
            if multiple_choice == 'Y' or 'y' or 'yes' or 'Yes':
                algorithms.ConstraintRelaxation.run_multiple_times()
            else:
                print('Okay ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ ') 
                exit()       
            
    elif algo_choice not in ['1', '2', '3']:
        print("Please make a choice between 1 and 3")
