class Battery:

    def __init__(self, id, x, y, capacity):
        """
        Initialize attributes of battery
        """

        self.id = id
        self.x = x
        self.y = y
        self.coordinates= (x, y)
        self.capacity = capacity
        self.houses = []
        self.houses_to_battery = []
        self.housesid_to_battery = []

        self.batt_costs = 0

    def __str__(self):
        return f"location:{self.coordinates},\ncapacity: 1507.0,\nhouses: "       


    def add_house_info(self, house):
        house_info = {}

        house_info["location"] = house.coordinates

        self.houses.append(house_info)

        house_info["output"] = house.maxoutput
        
        self.houses.append(house_info)

        house_info["cables"] = house.cables

        self.houses.append(house_info)

    def battery_cost_calculation():
        total_costs_bat = 0
        total_costs_bat = len(batteries) * 5000
        return total

    def connect_house(self, house):
        """
        Connects house to battery and substracts output from the capacity
        """

        self.houses_to_battery.append(house)
        self.housesid_to_battery.append(house.id)
        self.capacity -= house.maxoutput


    def remove_house(self, house):
        if house in self.houses_to_battery:
            self.houses_to_battery.remove(house)
            self.housesid_to_battery.remove(house.id)
            self.capacity += house.maxoutput
             

    def status(self, house):
        """
        Checks battery status
        """

        if house.maxoutput < self.capacity:
            return True

    def clear(self, house):

        self.houses_to_battery = []
        self.housesid_to_battery = []
        self.capacity = int(1507.0)
        self.batt_costs = 0
        self.houses = []