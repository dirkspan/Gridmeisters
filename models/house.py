from . import battery
from . import cables
import copy
from copy import deepcopy

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
        self.coordinates = (x, y)
        self.route = (None, None)
        self.costs = 0
        self.cables = []


    def add_costs(self, battery):
        """
        Calculates costs of house to battery
        """
        x_dist = abs(self.x - battery.x)
        y_dist = abs(self.y - battery.y)

        house_costs = (x_dist + y_dist) * 9 

        self.costs += house_costs    

    def route_calc(self, battery):

        cable = cables.Cable(self.x, self.y)

        self.cables.append(cable)

        temp_x = self.x
        temp_y = self.y

        while temp_x != battery.coordinates[0] or temp_y != battery.coordinates[1]:

            if temp_x < battery.coordinates[0]:
                cable = cables.Cable(temp_x + 1, temp_y)
                temp_x += 1
                self.cables.append(cable)

            elif temp_x > battery.x:
                cable = cables.Cable(temp_x - 1, temp_y)
                temp_x -= 1
                self.cables.append(cable)

            elif temp_y > battery.y:
                cable = cables.Cable(temp_x, temp_y - 1)
                temp_y -= 1
                self.cables.append(cable)

            elif temp_y < battery.y:
                cable = cables.Cable(temp_x, temp_y + 1)
                temp_y += 1
                self.cables.append(cable)               

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
        

    def __str__(self):
        return f"location: {self.coordinates}\noutput: {self.maxoutput}\ncables: ["   





    
    