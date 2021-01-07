import csv
from .battery import *
from .house import *

class Graph():

    def __init__(self, data):
        pass

    def load_nodes(self, data):

        nodes = {}
        

        with open('district-1_batteries.csv', 'r') as battery_data:
            battery_reader = csv.DictReader(battery_data)
            
            for row in battery_reader:
                battery = Battery(int(row[0], row[1], row[2], row[3], row[4])

                nodes[int(row[0])] = battery

        print(nodes)
        
                
                # {id: battery,}
        # with open('district-1_houses.csv', 'r') as house_data:
        #     house_reader = csv.DictReader(house_data)

        # {battery: house}

        # nodes[]
 