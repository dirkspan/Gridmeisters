from code.classes.cable import Cable
from random import shuffle


def random(grid):
    max_iterations = 1000
    for i in rand(max_iterations):
        try:
            grid.clear_cables()
            rand_grid = random_grid(grid)
            return rand_grid
        except KeyError:
            print(f"No solution found, trying it for the {i}th time")
    print("no solution found")

def random_grid(grid):
    batteries= grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    houses = grid.get_houses
    hkeys = list(houses.keys())
    shuffle(hkeys)

    j=0
    for i in range(len(hkeys)):
        cable=Cable(houses[hkeys[i]].get_id())
        cable.add_batt(batteries[bkey[j]].get_id())
        cable.add_route(houses[hkeys[i]].get_coord(), batteries[bkey[j]].get_coord())
        grid.add_cable(cable)
        i += 1
    
    return grid
