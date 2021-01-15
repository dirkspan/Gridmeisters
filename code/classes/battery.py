class Battery:

    def __init__(self, id, coordinate, capaciteit):
        """
        Initialize attributes of battery
        """

        self.id = id
        self.coordinate = (x,y)
        # self.x = x
        # self.y = y
        self.capaciteit = capaciteit

        # deze lijst gaat descending gesorteerd worden
        self.houses_to_battery = []
        self.connect = False
        self.battery_full = False

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapaciteit: {self.capaciteit}\n"       

    def is_possible(self, house):
        """
        Checks if house can be connected to the battery
        """

        if self.capaciteit > house.maxoutput:
            self.connect = True
        else:
            self.connect = False

    def connect_house(self, house, battery):
        """
        Connects house to battery and substracts output from the capacity
        """

        if self.connect == True:

            self.houses_to_battery.append(house)
            self.capaciteit -= house.maxoutput

    def status(self, house, battery):
        """
        Hier moeten we gaan kijken of het huis dat we aan de batterij willen koppelen mogelijk is
        
        Als het potentiele huis dat toegevoegd moet worden te groot is voor de overige ruimte in de
        batterij dan status = True, batterij is vol
        """

        if house.maxoutput > self.capaciteit:
            self.battery_full = True

    def get_most_costs(self, battery):
        """
        Returns highest costs of house grid to battery
        """

        return max(self.houses_to_battery)


    def remove_house(self, house, battery):
        """
        Removes house from the connection to battery and adds output back to capacity
        """

        self.houses_to_battery.pop(house)
        self.capaciteit += house.maxoutput
















    # def distance_x(self, house):
    #     house_x = house.x 
    #     self.dis_x_to_house = house.x - self.x   
        
    # def distance_y(self, house):
    #     house_y = house.y
    #     self.dis_y_to_house = house_y - self.y
                 