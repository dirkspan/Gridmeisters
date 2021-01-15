class Cable:

    def __init__(self):
        cable_route = []
        

    def add_route(self, house, battery):
        self.cable_route.append((house.x, house.y))
        self.cable_route.append((house.x, battery.y))
        self.cable_route.append((battery.x, battery.y))
        return cable_route

    def coordinates_cables(self, house, battery):

        route = []

        # start is house, end is battery
        current_x_cor = house.x
        end_x= battery.x
        current_y_cor = house.y
        end_y = battery.y

        while current_y_cor < end_y:
            route.append((current_x_cor, current_y_cor))
            current_y_cor += 1

        while current_x_cor <= end_x:
            route.append((current_x_cor, current_y_cor))
            current_x_cor += 1

        return route

    def return_cables(self):
        return coordinate_cables ()
