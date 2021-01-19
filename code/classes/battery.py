class Battery:

    def __init__(self, id, x, y, capacity):
        """
        Initialize attributes of battery
        """

        self.id = id
        self.x = x
        self.y = y
        self.capacity = capacity
        self.houses_to_battery = []
        self.temp_houses_to_battery = []
        self.battery_full = False
        self.coordinates= (x, y)
        self.shared_costs = 0


    def __str__(self):
<<<<<<< HEAD
        return f"Battery:{self.id}\ncoordinates: {self.coordinates}\ncapaciteit: {self.capaciteit}\n"       
=======
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapacity: {self.capacity}\n"       
>>>>>>> 37ec13e2e347264dd10d6d78ec363240ebe736fe


    def connect_house(self, house):
        """
        Connects house to battery and substracts output from the capacity
        """

        self.houses_to_battery.append(house)
        self.temp_houses_to_battery.append(house.id)
        self.capacity -= house.maxoutput


    def remove_house(self, house):

        self.houses_to_battery.remove(house)
        self.temp_houses_to_battery.remove(house.id)
        self.capacity += house.maxoutput
             

    def status(self, house):
        """
        Checks battery status
        """

        if house.maxoutput > self.capacity:
            self.battery_full = True
<<<<<<< HEAD
=======


>>>>>>> 37ec13e2e347264dd10d6d78ec363240ebe736fe


    def calc_shared_costs(self, house):
        for k in self.houses_to_battery:
            house_costs = k.costs
            house_costs += house_costs
            self.shared_costs = house_costs