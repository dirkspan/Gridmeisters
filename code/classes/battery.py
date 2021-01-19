class Battery:

    def __init__(self, id, x, y, capaciteit):
        """
        Initialize attributes of battery
        """

        self.id = id
        self.x = x
        self.y = y
        self.capaciteit = capaciteit
        self.houses_to_battery = []
        self.temp_houses_to_battery = []
        self.battery_full = False
        self.coordinates= (x, y)
        self.shared_costs = 0


    def __str__(self):
        return f"Battery:{self.id}\ncoordinates: {self.coordinates}\ncapaciteit: {self.capaciteit}\n"       


    def connect_house(self, house):
        """
        Connects house to battery and substracts output from the capacity
        """

        self.houses_to_battery.append(house)
        self.temp_houses_to_battery.append(house.id)
        self.capaciteit -= house.maxoutput


    def remove_house(self, house):

        self.houses_to_battery.remove(house)
        self.temp_houses_to_battery.remove(house.id)
        self.capaciteit += house.maxoutput
             

    def status(self, house):
        """
        Checks battery status
        """

        if house.maxoutput > self.capaciteit:
            self.battery_full = True


    def calc_shared_costs(self, house):
        for k in self.houses_to_battery:
            house_costs = k.costs
            house_costs += house_costs
            self.shared_costs = house_costs