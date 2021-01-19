import battery

class House(object):

    def __init__(self,id, x, y, maxoutput):
        """
        Initializes attributes of house
        """

        self.id = id
        self.x = x
        self.y = y
        self.maxoutput = maxoutput
        self.connected_to = None

        # bas had toch gelijk dit is beter
        self.coordinates = (x, y)
        self.route = (None, None)

        self.cables = []

    

    def connect_to_battery(self, battery):
        """
        Connects battery to a house
        """

        self.connected_to = battery

    def deconnect_to_battery(self, battery):
        """
        Deconnects battery
        """

        self.connected_to = None    

    # def route(self, house, battery)

    #     route = []

    #     # start is house, end is battery
    #     current_x_cor = coordinate_house[0]
    #     end_x= coordinate_battery[0]
    #     current_y_cor = coordinate_house[1]
    #     end_y = coordinate_battery[1]

    #     while current_y_cor < end_y:
    #         route.append((current_x_cor, current_y_cor))
    #         current_y_cor += 1

    #     while current_x_cor <= end_x:
    #         route.append((current_x_cor, current_y_cor))
    #         current_x_cor += 1

    #     return route
        
    def calc_costs(self, battery):
        """
        Calculates costs of house to battery
        """
        costs = abs((self.x+self.y) - (battery.x+battery.y))*9
        return costs


    def __str__(self):
        return f"House:{self.id}\nx: {self.x}\ny: {self.y}\nmaxoutput: {self.maxoutput}\n\nbattery:{self.connected_to}\n"   





    
    