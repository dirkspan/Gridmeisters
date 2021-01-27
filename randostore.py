def random_algorithm():
    """
    Connects each house randomly to a battery
    """

    count = 0

    tot_rand_costs = 0

    random.shuffle(houses)

    for battery in batteries:
        count = 0
        for house in houses:

            while battery.status(house) == True and house.connected_to == None:

                battery.connect_house(house)
                house.route_calc(battery)
                house.add_costs(battery)
                tot_rand_costs = tot_rand_costs + house.costs

                house.connect_to_battery(battery)
                count += 1
        print (count)
    if count == 150:
        return tot_rand_costs 

    # print(f"kosten!:{tot_rand_costs}")


[83, 11, 35, 130, 128, 60, 28, 3, 90, 109, 147, 85, 100, 104, 17, 7, 141, 114, 25, 16, 96, 67, 115, 71, 113, 88, 30, 18, 121, 70]
30
[19, 132, 55, 123, 2, 134, 140, 142, 72, 22, 66, 107, 110, 32, 4, 126, 56, 136, 58, 8, 64, 129, 37, 73, 69, 24, 98, 99, 92, 10]
30
[36, 117, 29, 42, 34, 50, 138, 108, 95, 51, 6, 78, 101, 1, 76, 116, 47, 41, 122, 144, 143, 77, 74, 40, 103, 94, 54, 82, 39, 112]
30
[62, 105, 15, 106, 53, 5, 65, 137, 97, 119, 26, 46, 124, 33, 61, 102, 79, 45, 148, 84, 131, 91, 118, 86, 111, 135, 13, 150, 127, 93]
30
[31, 49, 27, 43, 149, 80, 75, 81, 87, 89, 48, 38, 12, 133, 59, 9, 44, 68, 21, 120, 23, 63, 145, 125, 14, 146, 139, 57, 20, 52]