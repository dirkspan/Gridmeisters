
class Grid(object):

    def __init__(self, id, x_max, y_max):
      
        self._id = id
        self._x_max = x_max
        self._y_max = y_max
        self._cables = {}
        self._batteries = {}
        self._houses = {}

    def __str__(self):
        
        batteries = ""
        for key in self._batteries:
            if not batteries:
                batteries += "\n" + self.get_battery(key).__str__()
            else:
                batteries += "\n\n" + self.get_battery(key).__str__()

        houses = ""
        for key in self._houses:
            if not houses:
                houses += "\n" + self.get_house(key).__str__()
            else:
                houses += "\n\n" + self.get_house(key).__str__()

        cables = ""
        for key in self._cables:
            if not cables:
                cables += "\n" + self.get_cable(key).__str__()
            else:
                cables += "\n\n" + self.get_cable(key).__str__()

        return (f"District: {self._id}\nx max: {self._x_max}\ny max: {self._y_max}\n\nbatteries:{batteries}\n\n"
                f"houses:{houses} \n\ncables:{cables}")



    def get_id(self):
        
        return self._id

    def get_max(self):
       
        return self._x_max, self._y_max

    def get_house(self, id):
       
        return self._houses[id]

    def get_houses(self):
        
        return self._houses

    def get_battery(self, id):
       
        return self._batteries[id]

    def get_batteries(self):
        
        return self._batteries

    def get_cable(self, cable_id):
        
        return self._cables[cable_id]

    def get_cables(self):
        
        return self._cables

    def tot_len(self):
        # Calculate total length of all cables.
       
        len = 0
        for key in self._cables:
            len += self._cables[key].get_length()
        return len

    # Mutator methods (setters)
    def add_house(self, house):
        
        if house.get_id() not in self._houses:
            self._houses[house.get_id()] = house
        else:
            print("Error: Key already in _houses")

    def add_battery(self, battery):
        
        if battery.get_id() not in self._batteries:
            self._batteries[battery.get_id()] = battery
        else:
            print("Error: Key already in self._batteries")

    def add_cable(self, cable):
      
        cable_id = cable.get_id()
        self._cables[cable_id] = cable

    def rem_cable(self, key):
       
        del self._cables[key]

    def clear_cables(self):
      
        self._cables = {}
        for key in self._batteries:
            self._batteries[key].reset_cap()