# test document voor het maken van de route X Sofie
class Cable(object):

    def __init__(self, cable_id):
       
        self.id = cable_id
        self.battery_id = ""
        self.route = []

    def __str__(self):
        
        return (f"Cable: {self.id}\n"
                f"From house: {self.id} to battery {self.battery_id}\nRoute: {self.route}")

    # def get_id(self):
     
    #     return self._id

    # def get_batt(self):
     
    #     return self._battery_id


    # def get_length(self):
        
    #     start = self._route[0]
    #     end = self._route[-1]
    #     return abs(start[0] - end[0]) + abs(start[1] - end[1])

    # def get_route(self):
    
    #     return self._route

    # def add_batt(self, batt_id):
        
    #     self._battery_id = batt_id

    # def add_house(self, house_id):
       
    #     self._house_id = house_id

    # def add_route(self, house, battery):
     
    #     self._route.append((house[0], house[1]))
    #     self._route.append((battery[0], house[1]))
    #     self._route.append((battery[0], battery[1]))

    # def change_route(self, start, end):
       
    #     self._route = []
    #     self.add_route(start, end)