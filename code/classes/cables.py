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
            while temp_x is not 38 and temp_y is not 12:
                
                if temp_x < 38:
                    temp_x += 1
                    house_x_dist.append(temp_x)

                if temp_x > 38:
                    temp_x -= 1
                    house_x_dist.append(temp_x)
                if temp_x == 38 and temp_y != 12:
                    house_x_dist.append(temp_x)
               
                    
                if temp_y < 12:
                    temp_y += 1
                    house_y_dist.append(temp_y)
                if temp_y > 12:
                    temp_y -= 1
                    house_y_dist.append(temp_y)
                if temp_y == 12 and temp_x != 38:
                    house_y_dist.append(temp_y)
                    
                    

        # return house_x_dist
        return house_y_dist
             


