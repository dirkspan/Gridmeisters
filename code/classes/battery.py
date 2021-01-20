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
        self.cables = {}




    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapacity: {self.capacity}\n"       


    def coordinates_cables(self, house):

        current_x = house.x
        end_x= self.x
        current_y = house.y
        end_y = self.y
            
        if current_y < end_y:
            while current_y < end_y:
                self.cables[house.id] = current_x
                current_y += 1

        elif current_y > end_y:
            while current_y > end_y:
                self.cables[house.id] = current_x
                current_y -= 1

        if current_x < end_x:
            while current_x <= end_x:
                self.cables[house.id] = current_x
                current_x += 1

        elif current_x > end_x:
            while current_x >= end_x:
                self.cables[house.id] = current_x
                current_x -= 1
    
        return self.cables

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
