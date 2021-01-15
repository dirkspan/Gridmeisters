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
        # self.possible = False
        self.connected_to = None
<<<<<<< HEAD
    
    # def check(self, battery:
    #     if self.maxoutput < battery.capaciteit:
    #         self.possible = True

    def connect_to_battery(self, house ,battery):
=======
       
    def connect_to_battery(self, house, battery):
>>>>>>> 7a8bf59927d25e4cb763521d5bef377ea7475e43
        """
        Connects battery to a house
        """

        self.connected_to = battery
        
    def calc_costs(self, house, battery):
        """
        Calculates costs of house to battery
        """

        self.connected_to = battery
        costs = abs((self.x+self.y) - (battery.x+battery.y))*9
        return costs


    def __str__(self):
        return f"House:{self.id}\nx: {self.x}\ny: {self.y}\nmaxoutput: {self.maxoutput}\n\nbattery:{self.connected_to}\n"   





    
    