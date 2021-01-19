class Cable:

    def __init__(self):
        cable_route = []
        

    def add_route(self, house, battery):
        self.cable_route.append((house.x, house.y))
        self.cable_route.append((house.x, battery.y))
        self.cable_route.append((battery.x, battery.y))
        return cable_route

    def coordinates_cables(self, house, battery):

        current_x = house.x
        end_x= battery.x
        current_y = house.y
        end_y = battery.y
            
        if current_y < end_y:
            while current_y < end_y:
                house.cables.append((current_x, current_y))
                current_y += 1

        elif current_y > end_y:
            while current_y > end_y:
                house.cables.append((current_x, current_y))
                current_y -= 1

        if current_x < end_x:
            while current_x <= end_x:
                house.cables.append((current_x, current_y))
                current_x += 1

        elif current_x > end_x:
            while current_x >= end_x:
                house.cables.append((current_x, current_y))
                current_x -= 1
    
        return house.cables

        # route = []

        # # start is house, end is battery
        # current_x = house.x
        # end_x = battery.x
        # current_y = house.y
        # end_y = battery.y

        # if current_y < end_y:
        #     while current_y < end_y:
        #         route.append((current_x, current_y))
        #         current_y += 1
        # elif current_y > end_y:
        #     while current_y > end_y:
        #         route.append((current_x, current_y))
        #         current_y -= 1

        # if current_x < end_x:
        #     while current_x <= end_x:
        #         route.append((current_x, current_y))
        #         current_x += 1
        # elif current_x > end_x:
        #     while current_x >= end_x:
        #         route.append((current_x, current_y))
        #         current_x -= 1

        # return route

    def return_cables(self):
        return coordinate_cables ()
