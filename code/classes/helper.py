import random
import load_data



def random_battery(batteries):

    curr_battery = random.choice(batteries)

    return curr_battery

def return_max_dist(batteries):

    battery = random_battery(batteries)

    connections = battery.houses_to_battery

    dictionary = {}

    for j in connections:

        tot_costs = j.calc_costs(battery)

    return connections


def hillclimber(batteries, houses):

    for j in range(1000):

        for battery in batteries:

            curr_battery = battery

            for curr_house in curr_battery.houses_to_battery:

                for next_house in houses:

                    if next_house not in curr_battery.houses_to_battery:

                        # if curr_house is not next_house and curr_house.calc_costs(curr_battery) > next_house.calc_costs(curr_battery):
                            
                        next_battery = next_house.connected_to

                        if logic_swap(curr_battery, curr_house, next_battery, next_house) == True:

                            if curr_house.maxoutput + curr_battery.capacity > next_house.maxoutput and next_house.maxoutput + next_battery.capacity > curr_house.maxoutput:
                        
                                # STAP 1:
                                if curr_house in curr_battery.houses_to_battery:
                                # remove current house van current battery
                                    curr_battery.remove_house(curr_house)
                                    curr_house.deconnect_to_battery(curr_battery)

                                # connect next house aan current battery
                                curr_battery.connect_house(next_house)
                                next_house.connect_to_battery(curr_battery)

                                # STAP 2:
                                # remove next house van next battery
                                next_battery.remove_house(next_house)
                                next_house.deconnect_to_battery(next_battery)

                                # connect current house aan next battery
                                next_battery.connect_house(curr_house)
                                curr_house.connect_to_battery(next_battery)

def logic_swap(curr_battery, curr_house, next_battery, next_house):


    """

    Vanuit current battery kijken of er betere opties zijn

    In current battery zitten de volgende huizen: dit zijn current_houses

    De current_houses gaan we vergelijken met de next_houses

    Als de distance van next_house naar current_battery korter is dan de distance van
    current_house naar currenty_battery

    Current_house moet weg uit currenty battery, en next_house moet hiervan in de plaats

    Current_house moet naar de batterij waar next_house mee verbonden was

    Alleen als deze distance, de vorige distance overschrijdt heeft het geen zin..

    En deze distance is van: current_house naar next_battery vs next_house met next_battery:

    """

    # hoe het er nu in staat
    # dist1 = abs(curr_house.coordinates[0] - curr_battery.coordinates[0]) + abs(curr_house.coordinates[1] - curr_battery.coordinates[1])  

    # hoe het na de swap wordt
    # dist2 = abs(curr_house.coordinates[0] - next_battery.coordinates[0]) + abs(curr_house.coordinates[1] - next_battery.coordinates[1])    

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

    # dist1 = curr_house.calc_costs(curr_battery) - next_house.calc_costs(curr_battery)

    #                                             - curr_house.calc_costs(next_batter) -> +? 

    # dist2 = curr_house.calc_costs(next_battery) - next_house.calc_costs(next_battery)
    #         next                                                        curr_       -> +?

    #         d1 - d2 -> + = swappen 
    
    #         curr house batt en +  next house batt <
    #         curr house next batt + next house curr batt


