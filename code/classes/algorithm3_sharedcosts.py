"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""
import load_data
import house
import battery
import cables 
import random
import helper
import matplotlib.pyplot as plt

from matplotlib import style

# read in all data
reader = load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

# list for all unused houses
unused_houses = []

#set costs to 0
costs = 0


for house in houses:

    # keep track of distances between each house and battery
    dist_dict = {}

    # keeps track on wether battery is useable
    keep_track = []

    # empty list of coordinates
    cables_coordinates = []

    for battery in batteries:
        
        # battery is not full
        if battery.status(house) == True:

            distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

            dist_dict[battery] = distance

            # save list
            keep_track.append(1)

        else:
            keep_track.append(0)

    if keep_track.count(1) == 0:

        unused_houses.append(house)

    else:

        # return closest distance of a house to the battery
        closest_distance = min(dist_dict.items(), key=lambda x: x[1])


        closest_battery= closest_distance[0]
        battery = closest_battery

        route = (house.x, battery.y)

        # connects house to battery and vice versa
        house.connect_to_battery(battery)
        battery.connect_house(house)
        battery.add_costs(house)

        # print(battery.costs)


helper.hillclimber(batteries, houses)



# curr_unused_houses = []

# if len(unused_houses) <= 1:

#     # curr_battery = random.choice(batteries)
#     for battery in batteries:

#         costs = battery.costs
#         print(costs)
#         # tracker = []

        # for house in houses:

        #     for curr_house in battery.houses_to_battery:

        #         if house not in battery.houses_to_battery:

        #             if curr_house is not house and curr_house.calc_costs(battery) > house.calc_costs(battery):
                        
        #                 if curr_house.maxoutput + battery.capacity > house.maxoutput:
                            
        #                     # print(f"old{curr_house.calc_costs(curr_battery)}")
        #                     battery.remove_house(curr_house)

        #                     battery.connect_house(house) 

        #                     tracker.append(1)

        #                 else:
        #                     tracker.append(0)

        # if tracker.count(1) == 0:
        #     curr_unused_houses.append(house)



# if len(unused_houses) <= 1:
    
#     for battery in batteries:

#         for j in battery.houses_to_battery:

#             if j is not house:

#                 if j.calc_costs(battery) > house.calc_costs(battery):

#                     # old_costs = j.calc_costs(battery)
#                     # new_costs = house.calc_costs(battery)

#                     # # print(f"Old:{old_costs}")
#                     # # print(f"New:{new_costs}")

#                     # old = houses.index(house)
#                     # new = battery.houses_to_battery.index(j)

#                     # houses.append(j)
#                     battery.houses_to_battery.append(house)

#                     # old, new = new, old

#                     # temp = old
#                     # old = new
#                     # new = temp


#                     print(battery.temp_houses_to_battery)       


# if len(unused_houses) <= 1:

#     i = -1
#     for battery in batteries:

#         i += 1
#         for house in battery.houses_to_battery:

#             colors = ['c', 'k', 'b', 'g', 'r']

#             house_x = house.x
#             house_y = house.y

#             battery_x = battery.x
#             battery_y = battery.y

#             cutting_point_x = house.x
#             cutting_point_y = battery.y

#             x = [house_x, cutting_point_x, battery_x]
#             y = [house_y, cutting_point_y, battery_y]

#             ax = plt.subplot(111)

#             houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
#             batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

#             plt.plot(x,y, color= colors[i])

#             plt.savefig("testing.png")
   








        
# # we hebben alle matches gevonden
# if len(unused_houses) == 0:

# # print uitkomst voor alle 5 batterijen
# for battery in batteries:

#     # print(f"This is battery {battery.id} Houses: {battery.temp_houses_to_battery}")
#     print(f"NEW BATTERY!!")
#     print(f"location: {battery.x,battery.y}")
#     print(f"capacity: 1507.0")

#     for house in battery.houses_to_battery:

#         # cable.coordinates_cables(house, battery)

#         # start is house, end is battery
#         current_x = house.x
#         end_x= battery.x
#         current_y = house.y
#         end_y = battery.y

#         # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
#         if current_y < end_y:
#             while current_y < end_y:
#                     house.cables.append((current_x, current_y))
#                     current_y += 1

#         elif current_y > end_y:
#             while current_y > end_y:
#                 house.cables.append((current_x, current_y))
#                 current_y -= 1

#         if current_x < end_x:
#             while current_x <= end_x:
#                 house.cables.append((current_x, current_y))
#                 current_x += 1

#         elif current_x > end_x:
#             while current_x >= end_x:
#                 house.cables.append((current_x, current_y))
#                 current_x -= 1

#         for tuple in house.cables:
#             # line_house = house.cables
#             if tuple not in cables_coordinates:
#                 cables_coordinates.append(tuple)

#         number_of_cables = int(len(cables_coordinates))
#         costs_all_cables_to_battery = number_of_cables * 9 
  

#         # prints output for each house, each coordinate of the cable
#         print(f"house ID: {house.id}")
#         print(f"location: {house.x,house.y},")
#         print(f"output: {house.maxoutput},")
#         print(f"cables:{house.cables}")

#     print("cable costs, cables shared:")
#     print(costs_all_cables_to_battery)

#     # costs for all batteries
#     costs = costs_all_cables_to_battery + (5000 * len(batteries))
#     print(f"all costs for complete district: {costs} ")
    
        
        

#     # print("all used coordinates")
#     # print(cables_coordinates)


if len(unused_houses) == 0:

    helper.hillclimber(batteries, houses)
    
    i = -1

    for battery in batteries:
        i += 1
        for house in battery.houses_to_battery:

<<<<<<< HEAD
            colors = ['c', 'k', 'b', 'g', 'r']

            house_x = house.x
            house_y = house.y

            battery_x = battery.x
            battery_y = battery.y
=======
        # colors = ['c', 'k', 'b', 'g', 'r']

        # house_x = house.x
        # house_y = house.y

        # battery_x = battery.x
        # battery_y = battery.y
>>>>>>> 9799632231017832d444d5b697998cc76b8b14ef

            cutting_point_x = house.x
            cutting_point_y = battery.y

            # line_house

            # plot line between house and cutting point 
            x = [house_x, cutting_point_x, battery_x]
            y = [house_y, cutting_point_y, battery_y]

<<<<<<< HEAD
            ax = plt.subplot(111)

            houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
            batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')


            plt.plot(x,y, color= colors[i])

            plt.savefig("testing6.png")

        
=======
        houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
        batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')


        # plot tuples as cables

    # all matches found, not a single house unused
    # if unused_houses == []:
        # print(f"{battery}: Houses: {len(battery.temp_houses_to_battery)}")

        # plt.plot(line_house, color= colors[i])




for house in houses:
    plt.plot(*zip(*house.cables))

# # plt.savefig("test3share.png")
# for house in houses:
#     plt.plot(*zip(*house.cables))
# plt.savefig("test3share.png")
#     plt.savefig("test3share.png")
>>>>>>> 9799632231017832d444d5b697998cc76b8b14ef
