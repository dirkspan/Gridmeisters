# from code.classes import *
from code.classes.load_data import Load_data
# from code.classes import plot
from code.classes.plot import plot
# from code.visualisation import *

if __name__ == "__main__":
    load_data = Load_data()
    houses = load_data.load_houses()