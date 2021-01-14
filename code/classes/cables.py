class Cable:

    def __init__(self):
        cable_route = []
        

    def add_route(self, house, battery):
        self.cable_route.append((house.x, house.y))
        self.cable_route.append((house.x, battery.y))
        self.cable_route.append((battery.x, battery.y))
        return cable_route

    # def return_cables(self):
    #     return cable_route
