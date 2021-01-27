import random
import models.load_data

def hillclimber(batteries, houses):
    """
    Hillclimber, goes through every connection already made
    to check if there are any better alternatives
    """

    for next_house in houses:

        for battery in batteries:

            curr_battery = battery
            
            for curr_house in curr_battery.houses_to_battery:

                if next_house not in curr_battery.houses_to_battery:
                        
                    next_battery = next_house.connected_to

                    if logic_swap(curr_battery, curr_house, next_battery, next_house) == True:

                        if output_swap(curr_battery, curr_house, next_battery, next_house) == True:

                            run_swap(curr_battery, curr_house, next_battery, next_house)

def run_swap(curr_battery, curr_house, next_battery, next_house):
    """
    Performs swap
    """

    if curr_house in curr_battery.houses_to_battery:

        # remove current house van current battery
        curr_battery.remove_house(curr_house)
        curr_house.disconnect_battery(curr_battery)

    # connect next house aan current battery
    curr_battery.connect_house(next_house)
    next_house.connect_to_battery(curr_battery)

    # remove next house van next battery
    next_battery.remove_house(next_house)
    next_house.disconnect_battery(next_battery)

    # connect current house aan next battery
    next_battery.connect_house(curr_house)
    curr_house.connect_to_battery(next_battery)                              
                                
def output_swap(curr_battery, curr_house, next_battery, next_house):
    """
    Check to see if swap is possible based on house output and capacity of battery
    """

    if curr_house.maxoutput + curr_battery.capacity > next_house.maxoutput and next_house.maxoutput + next_battery.capacity > curr_house.maxoutput:
        return True
    else:
        return False

def logic_swap(curr_battery, curr_house, next_battery, next_house):
    """
    Check to see if swap is profitable based on distance comparing
    """

    if curr_house and curr_battery and next_house and next_battery is not None:

        dist10 = abs(curr_house.coordinates[0] - next_battery.coordinates[0]) + abs(curr_house.coordinates[1] - next_battery.coordinates[1])  
        dist11 = abs(next_house.coordinates[0] - curr_battery.coordinates[0]) + abs(next_house.coordinates[1] - curr_battery.coordinates[1])  

        dist12 = abs(curr_house.coordinates[0] - curr_battery.coordinates[0]) + abs(curr_house.coordinates[1] - curr_battery.coordinates[1])
        dist13 = abs(next_house.coordinates[0] - next_battery.coordinates[0]) + abs(next_house.coordinates[1] - next_battery.coordinates[1])    

        dist2 = dist10 + dist11
        dist1 = dist12 + dist13

        if dist2 < dist1:
            return True
        else:
            return False    

def calculate_distance(house, battery):
    """
    Calculate distance from house to battery
    """

    
    distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

    return distance
