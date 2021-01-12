# test document voor het maken van de route X Sofie
class Cable(object):

    def __init__(self, cable_id):
        # cable class identification
        self.id = cable_id
        self.battery_id = ""
        self.route = []

    def __str__(self):
        # return string
        return (f"Cable: {self.id}\n"
                f"From house: {self.id} to battery {self.battery_id}\nRoute: {self.route}")

    def get_id(self):
        # return id of the cable
        return self.id

    def get_batt(self):
        # returns id of current battery
        return self.battery_id


    def get_length(self):
        # start of route is house and end is battery. 0 is the x coordinate and 1 is the y, so you get the length
        start = self.route[0]
        end = self.route[-1]
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def get_route(self):
        # return route
        return self._route

    def add_batt(self, batt_id):
        # identify battery as linked battery
        self.battery_id = batt_id

    def add_house(self, house_id):
        # identify house as current linked house
        self.house_id = house_id

    def add_route(self, house, battery):
        # identify route, first the coordinate of the house, then the vertices, with x of the bat and y of the house. last from the corner to the end
        self.route.append((house[0], house[1]))
        self.route.append((battery[0], house[1]))
        self.route.append((battery[0], battery[1]))

    def change_route(self, start, end):
        # empty route and add new route     
        self.route = []
        self.add_route(start, end)