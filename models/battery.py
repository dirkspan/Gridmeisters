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

    def __str__(self):
        return f"location:{self.coordinates},\n{self.capacity},\nhouses:"       

    def connect_house(self, house):
        """
        Connects house to battery and substracts output from the capacity
        """

        self.houses_to_battery.append(house)
        self.housesid_to_battery.append(house.id)
        self.capacity -= house.maxoutput

    def remove_house(self, house):
        """
        Removes house to battery and substracts output from the capacity
        """

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
        """
        Clears everything for next run
        """

        self.houses_to_battery = []
        self.housesid_to_battery = []
        self.capacity = int(1507.0)
        self.batt_costs = 0
        self.houses = []