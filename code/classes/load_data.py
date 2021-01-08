import csv
from battery import Battery
from house import House

class Load_data:

    def load_batteries(self):

        batteries = []
        
        with open('district-1_batteries.csv', 'r') as battery_data:
            battery_reader = csv.DictReader(battery_data)
        
            for row in battery_reader:
                id = int(row['id'])
                battery = Battery(int(row['id']), row['x'], row['y'], row['capaciteit'])
                batteries.append(battery)

        return batteries
                
    def load_houses(self):

        houses = []

        with open('district-1_houses.csv', 'r') as house_data:
            house_reader = csv.DictReader(house_data)

            for row in house_reader:
                house = House(int(row['id']), row['x'], row['y'], row['maxoutput'])
                houses.append(house)

        return houses
