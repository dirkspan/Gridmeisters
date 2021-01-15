class Cable:

    def __init__(self):
        cable_route = []
        

    def add_route(self, house, battery):
        self.cable_route.append((house.x, house.y))
        self.cable_route.append((house.x, battery.y))
        self.cable_route.append((battery.x, battery.y))
        return cable_route

    def cable_route(self, house, battery):

        house.coordinate = coordinate_house
        battery.coordinate = coordinate_battery
        # coordinate_house =[33, 7]
        # coordinate_battery=[38, 12]

        route = []

        # start is house, end is battery
        current_x_cor = coordinate_house[0]
        end_x= coordinate_battery[0]
        current_y_cor = coordinate_house[1]
        end_y = coordinate_battery[1]

        while current_y_cor < end_y:
            route.append((current_x_cor, current_y_cor))
            current_y_cor += 1

        while current_x_cor <= end_x:
            route.append((current_x_cor, current_y_cor))
            current_x_cor += 1

        return route

    # def return_cables(self):
    #     return cable_route
