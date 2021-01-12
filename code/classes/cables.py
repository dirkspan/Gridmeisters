import battery
import house
import load_data
import random

class Grid:

    def cables(self, houses, batteries):

        house_x_dist = []
        house_y_dist = []
        
        # rand_battery = random.choice(batteries)
        
        for house in houses:
            
            temp_x = house.x
            temp_y = house.y
            while house.x is not 38 and house.y is not 12:
                
                if temp_x < 38:
                    temp_x += 1
                    house_x_dist.append(temp_x)

                if temp_x > 38:
                    temp_x -= 1
                    house_x_dist.append(temp_x)
                if temp_x == 38:
                    break
                    

        return house_x_dist
             


