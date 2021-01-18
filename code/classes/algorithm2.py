"""
Gaat op zoek naar de dichtsbijzijnde x en y coordinaat
"""


import load_data
import house
import battery
import random

reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

all_batteries = []

for battery in batteries:
    all_batteries.append(battery)


i = 0

for j in range(200000):

    for house in houses:
        
        battery = all_batteries[i]

        battery.status(house, battery)
        
        if house.connected_to == None and battery.battery_full == False:

            if house.x == battery.x and house.y == battery.y:
                curr = battery.houses_to_battery

                if house not in curr:
                    battery.connect_house(house)
                    house.connect_to_battery(house, battery)

            elif house.x < battery.x and house.y == battery.y:
                house.x += 1

            elif house.x > battery.x and house.y == battery.y:
                house.x -= 1            

            elif house.x < battery.x and house.y < battery.y:
                house.x += 1
                house.y += 1
        
            elif house.x > battery.x and house.y < battery.y:
                house.x -= 1
                house.y += 1

            elif house.x == battery.x and house.y < battery.y:
                house.y += 1

            elif house.x == battery.x and house.y > battery.y:
                house.y -= 1

            elif house.x < battery.x and house.y > battery.y:
                house.x += 1
                house.y -= 1
        
            elif house.x > battery.x and house.y > battery.y:
                house.x -= 1
                house.y -= 1

        if battery.battery_full == True:
            break
           


 



# a = battery.houses_to_battery
# print(a)

# for j in a:
#     b =
#     print(b)
    









# i = 0
# house_costs = 10000

# # loop through houses
# for house in houses:

#     # start at first battery
#     battery = all_batteries[i]

#     next_house_costs = house.calc_costs(house, battery)

#     # checks to see if battery is full
#     battery.status(house, battery)

#     # move to next battery
#     if battery.battery_full == False:

#         if next_house_costs < house_costs: 

#             battery.is_possible(house)
#             battery.connect_house(house, battery)
#             house_costs = house.calc_costs(house, battery)
#             print(f"this is: {battery} with {battery.houses_to_battery}, output: {house.maxoutput} with costs: {house.calc_costs(house, battery)}") 