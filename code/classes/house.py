import battery

class House(object):

    def __init__(self,id, x, y, maxoutput):
        """
        Initializes attributes of house
        """

        self.id = id
        self.x = x
        self.y = y
        self.maxoutput = maxoutput
        self.connected_to = None

        # bas had toch gelijk dit is beter
        self.coordinates = (x, y)
        self.route = (None, None)
        self.costs = 0

    def connect_to_battery(self, battery):
        """
        Connects battery to a house
        """

        self.connected_to = battery

    def deconnect_to_battery(self, battery):
        """
        Deconnects battery
        """

        self.connected_to = None    
        
    def calc_costs(self, battery):
        """
        Calculates costs of house to battery
        """
        costs = abs((self.x+self.y) - abs(battery.x+battery.y))*9
        self.costs = costs


    def __str__(self):
        return f"House:{self.id}\ncoordinates: {self.y}\nmaxoutput: {self.maxoutput}\n\nbattery:{self.connected_to}\n"   





    
    