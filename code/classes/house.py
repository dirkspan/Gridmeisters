import battery

class House:

    def __init__(self,id, x, y, maxoutput):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.maxoutput = float(maxoutput)

    def __str__(self):
        return f"House:{self.id}\nx: {self.x}\ny: {self.y}\nmaxoutput: {self.maxoutput}\n"   

    # def cables(self):
    #     house_x_dist = []

    #     for house in houses:
    #         for battery in batteries:
    #             if house.x < battery.x:
    #                 house.x += 1
    #                 house_x_dist.append(house.x)
    #             if house.x > battery.x:
    #                 house.x -= 1
    #                 house_x_dist.append(house.x)
    #             if house.x == battery.x:
    #                 break





    
    