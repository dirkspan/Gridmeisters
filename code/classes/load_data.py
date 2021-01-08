import csv
from battery import Battery
from house import House

def load_batteries(self):

    self.batteries = []

    with open('data/district_1/district-1_batteries.csv', 'r') as battery_data:
        battery_reader = csv.DictReader(battery_data)
        
        for row in battery_reader:
            id = int(row['id'])
            battery = Battery(int(row['id']), row['x'], row['y'], row['capaciteit'])
            self.batteries.append(battery)

    return self.batteries
                
def load_houses(self):

    self.houses = []

    with open('data/district_1/district-1_batteries.csv', 'r') as house_data:
        house_reader = csv.DictReader(house_data)

        for row in house_reader:
            house = House(int(row['id']), row['x'], row['y'], float(row['maxoutput']))
            self.houses.append(house)

        return self.houses
