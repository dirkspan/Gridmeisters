import random
import copy

def random_assignment(graph, possibilities):
    """
    Randomly assign each node with one of the possibilities.
    """
    for node in graph.nodes.values():
        node.set_value(random.choice(possibilities))


def random_reconfigure_node(graph, node, possibilities):
    """
    Takes a node and assigns each node with one of the possibilities.
    """
    node.set_value(random.choice(possibilities))


def random_reconfigure_nodes(graph, nodes, possibilities):
    """
    Takes a list of nodes and assigns each node with one of the possibilities.
    """
    for node in nodes:
        random_reconfigure_node(graph, node, possibilities)


def random_reassignment(graph, possibilities):
    """
    Algorithm that reassigns nodes that are invalid until each node is valid.
    CAUTION: may run indefinitely.
    """
    new_graph = copy.deepcopy(graph)

    # Randomly assign a value to each of the nodes
    random_assignment(new_graph, possibilities)

    # Find nodes that are "violations" and have neighbours with same value
    violating_nodes = new_graph.get_violations()

    # While we have violations
    while len(violating_nodes):
        # Reconfigure violations randomly
        random_reconfigure_nodes(new_graph, violating_nodes, possibilities)

        # Find nodes that are violations
        violating_nodes = new_graph.get_violations()

    return new_graph

# example random algorithm


from classes.cable import Cable
from random import shuffle


def random(grid):
    """
    Do random algorithm, if random does not find a solution (not all houses are connected to a battery),
    do random again.
    :param grid: object
    :return: object
    """
    max_iterations = 1000
    for i in range(max_iterations):
        try:
            grid.clear_cables()
            rand_grid = random_grid(grid)
            return rand_grid
        except KeyError:
            print(f"grid not solved, trying again for the {i}th time")
    print("no solution found")


def random_grid(grid):
    """
    Connect each house to a random battery
    :param grid:
    :return:
    """

    batteries = grid.get_batteries()
    bkeys = list(batteries.keys())
    shuffle(bkeys)

    houses = grid.get_houses()
    hkeys = list(houses.keys())
    shuffle(hkeys)

    j = 0
    for i in range(len(hkeys)):
        if batteries[bkeys[j]].get_cap() > houses[hkeys[i]].get_max():
            batteries[bkeys[j]].red_cap(houses[hkeys[i]].get_max())
            cable = Cable(houses[hkeys[i]].get_id())
            cable.add_batt(batteries[bkeys[j]].get_id())
            cable.add_route(houses[hkeys[i]].get_coord(), batteries[bkeys[j]].get_coord())
            grid.add_cable(cable)
            i += 1

        else:
            i -= 1
            j += 1
            if j >= len(bkeys):
                j = 0
    return grid