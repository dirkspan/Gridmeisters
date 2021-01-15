class Battery:

    def __init__(self, id, x, y, capaciteit):
        """
        Initialize attributes of battery
        """

        self.id = id
        self.x = x
        self.y = y
        self.capaciteit = capaciteit

        # deze lijst gaat descending gesorteerd worden
        self.houses_to_battery = []
        self.houses_to_checked_battery_costs = []
        self.connect = False
        self.battery_full = False

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapaciteit: {self.capaciteit}\n"       


    def connect_house(self, house):
        """
        Connects house to battery and substracts output from the capacity
        """

        self.connect = True
        self.houses_to_battery.append(house)
        self.houses_to_checked_battery_costs.append(house.id)
        self.capaciteit -= house.maxoutput


    def remove_house(self, house):

        self.connect = False
        self.houses_to_battery.remove(house)
        self.capaciteit += house.maxoutput
             

    def status(self, house, battery):
        """
        Hier moeten we gaan kijken of het huis dat we aan de batterij willen koppelen mogelijk is
        
        Als het potentiele huis dat toegevoegd moet worden te groot is voor de overige ruimte in de
        batterij dan status = True, batterij is vol
        """

        if house.maxoutput > self.capaciteit:
            self.battery_full = True

    def houses_to_checked_battery_costs(self, house, battery):
        """
        Adds the costs of the grid to the battery to a list
        """

        costs = abs((self.x+self.y) - (house.x+house.y))*9
        return costs


