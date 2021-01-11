
class Grid(object):

    def __init__(self, id, x_max, y_max):
      
        self.id = id
        self.x_max = x_max
        self.y_max = y_max
        self.cables = {}
        self.batteries = {}
        self.houses = {}

    def __str__(self):
        
        batteries = ""
        for key in self.batteries:
            batteries += "\n" + self.get_battery(key).__str__()
           
        houses = ""
        for key in self.houses:
            houses += "\n" + self.get_house(key).__str__()
            

        cables = ""
        for key in self.cables:
            cables += "\n" + self.get_cable(key).__str__()

        return (f"District: {self._id}\nx max: {self._x_max}\ny max: {self._y_max}\n\nbatteries:{batteries}\n\n"
                f"houses:{houses} \n\ncables:{cables}")


    # def get_id(self):
        
    #     return self._id

    # def get_max(self):
       
    #     return self._x_max, self._y_max

    # def get_house(self, id):
       
    #     return self._houses[id]

    # def get_houses(self):
        
    #     return self._houses

    # def get_battery(self, id):
       
    #     return self._batteries[id]

    # def get_batteries(self):
        
    #     return self._batteries

    # def get_cable(self, cable_id):
        
    #     return self._cables[cable_id]

    # def get_cables(self):
        
    #     return self._cables

    
    # def add_cable(self, cable):
      
    #     cable_id = cable.get_id()
    #     self._cables[cable_id] = cable

    # def rem_cable(self, key):
       
    #     del self._cables[key]

    # def clear_cables(self):
      
    #     self._cables = {}
    #     for key in self._batteries:
    #         self._batteries[key].reset_cap()