
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

    def get_id(self):
        # id of the grid
        return self._id

    def get_max(self):
        # return maxes
        return self.x_max, self.y_max

    def get_house(self, id):
        # return house in dic with id
        return self.houses[id]

    def get_houses(self):
        # return houses
        return self.houses

    def get_battery(self, id):
        # return battery in dictionary with id
        return self.batteries[id]

    def get_batteries(self):
        # return batteries
        return self.batteries

    def get_cable(self, cable_id):
        # get cable in dictionary with cable id
        return self.cables[cable_id]

    def get_cables(self):
        # return cables
        return self.cables

    
    def add_cable(self, cable):
        # add cable in dictionary with cable id
        cable_id = cable.get_id()
        self.cables[cable_id] = cable

    def rem_cable(self, key):
        # cables, coupled with key
        del self.cables[key]

    def clear_cables(self):
        # clear cables dictionary, for all batteries reset capacity
        self.cables = {}
        for key in self.batteries:
            self.batteries[key].reset_cap()