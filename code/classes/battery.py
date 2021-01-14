class Battery:

    def __init__(self, id, x, y, capaciteit):
        self.id = id
        self.x = x
        self.y = y
        self.capaciteit = capaciteit
        self.houses_to_battery = []
        # self.dis_x_to_house = dis_x_to_house
        # self.dis_y_to_house = dis_y_to_house
        self.connect = False

    def __str__(self):
        return f"Battery:{self.id}\nx: {self.x}\ny: {self.y}\ncapaciteit: {self.capaciteit}\n"       

    def is_possible(self, house):
        if self.capaciteit > house.maxoutput:
            self.connect = True
        else:
            self.connect = False

    def connect_house(self, house, battery):
        if self.connect == True:

            # self.houses_to_battery.append((house.x, house.y))
            # self.houses_to_battery.append((house.x, battery.y))
            # self.houses_to_battery.append((battery.x, battery.y))
            self.houses_to_battery.append(house.id)
            self.capaciteit -= house.maxoutput
        # else:
        #     print(f"This is not possible with {house}")
        #     return 0


    # def distance_x(self, house):
    #     house_x = house.x 
    #     self.dis_x_to_house = house.x - self.x   
        
    # def distance_y(self, house):
    #     house_y = house.y
    #     self.dis_y_to_house = house_y - self.y
                 