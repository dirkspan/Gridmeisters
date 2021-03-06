import csv
from .battery import Battery
from .house import House
from sys import argv

class Load_data:

    def load_batteries(self):
        """
        Loads battery data
        """

        batteries = []
        
        with open(argv[1], 'r') as battery_data:
            battery_reader = csv.DictReader(battery_data)
        
            for row in battery_reader:
                battery = Battery(int(row['id']), int(row['x']), int(row['y']), float(row['capaciteit']))
                batteries.append(battery)

        return batteries
                
    def load_houses(self):
        """
        Loads house data
        """

        houses = []

        with open(argv[2], 'r') as house_data:
            house_reader = csv.DictReader(house_data)

            for row in house_reader:
                house = House(int(row['id']), int(row['x']),int(row['y']), float(row['maxoutput']))
                houses.append(house)

        return houses
