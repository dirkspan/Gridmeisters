import battery
import house

class Grid:

    def cables(self):

        house_x_dist = []

        for house in houses:
            for battery in batteries:
                if house.x < battery.x:
                    house.x += 1
                    house_x_dist.append(house.x)
                if house.x > battery.x:
                    house.x -= 1
                    house_x_dist.append(house.x)
                if house.x == battery.x:
                    break
                
        return house_x_dist        


