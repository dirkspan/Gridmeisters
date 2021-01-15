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

all_houses = []
for house in houses:
    all_houses.append(house.x)


i = 0
for house in houses:

    battery = all_batteries[i]

    if battery.battery_full == False:
        
        if temp_house_x < battery.x:
            temp_house_x += 1

        if temp_house_x > battery.x:
            temp_house_x -= 1

        if temp_house_y > battery.y:
            temp_house_y -= 1

        if temp_house_y < battery.y:
            temp_house_y += 1

        if temp_house_x == battery.x and temp_house_y == battery.y:     
            # check if connection can be made
            battery.is_possible(house)

            # checks to see if battery is full
            battery.status(house, battery)

            # connect house to battery
            if battery.connect == True:

                battery.connect_house(house, battery)
                print(f"this is: {battery} with {battery.houses_to_battery}, output: {house.maxoutput} with costs: {house.calc_costs(house, battery)}") 
    else:
        break






i = 0
house_costs = 10000

# loop through houses
for house in houses:

    # start at first battery
    battery = all_batteries[i]

    next_house_costs = house.calc_costs(house, battery)

    # checks to see if battery is full
    battery.status(house, battery)

    # move to next battery
    if battery.battery_full == False:

        if next_house_costs < house_costs: 

            battery.is_possible(house)
            battery.connect_house(house, battery)
            house_costs = house.calc_costs(house, battery)
            print(f"this is: {battery} with {battery.houses_to_battery}, output: {house.maxoutput} with costs: {house.calc_costs(house, battery)}") 