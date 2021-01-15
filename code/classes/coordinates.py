import house
import battery


class Coordinates:

    def __init__(self, route, all_coordinates):
        """
        Initialize attributes of Coordinate
        """

        self.route = []
        self.coordinate_house = coordinate_house
        self.coordinate_battery = coordinate_battery
        self.coordinate_corner = coordinate_corner

    def coordinate_house(self, house):

        coordinate_house = []
        coordinate_house.append(house.x)
        coordinate_house.append(house.y)
        
        return coordinate_house

    def coordinate_battery(self, battery):

        coordinate_battery = []
        coordinate_battery.append(battery.x)
        coordinate_battery.append(battery.y)

        return coordinate_battery

    def coordinate_corner(self, house, battery):
        
        coordinate_corner = []

        coordinate_corner.append(house.x)
        coordinate_corner.append(house.y)

        return coordinate_corner



    def route(self, house, battery):
        """
        Hier stoppen we alle coordinaten van , zoals benodigt voor json output.

        """
        route = []
        # startpunt is huis
        coordinate_house = str(coordinate_house[1], coordinate_house[2])
       

        #

        #
    