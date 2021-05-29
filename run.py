""" Runs Direct Utility Estimation agent on given Grid World """

import sys
from grid import *
from due_tabular import solve_tabular
from due_fa import solve_fa


def run(agent, grid, policy):
    # run given agent with the required grid
    # get correct grid map and its terminals
    if grid == 1:
        grid_map, terminals = get_world_1()
    elif grid == 2:
        grid_map, terminals = get_world_2()
    else:
        grid_map, terminals = get_world_3()
    # call the required agent
    if agent == 1:
        solve_tabular(grid_map, terminals, policy)
    else:
        solve_fa(grid_map, terminals, policy)


if __name__ == '__main__':
    # parse arugments
    if len(sys.argv) != 4:
        exit(-1)
    agent = sys.argv[1]
    grid = sys.argv[2]
    policy_file = sys.argv[3]
    # read policy from file
    policy = list()
    with open(policy_file) as f:
        for line in f:
            policy.append(line.rstrip().split())
    # call main driver
    run(agent, grid, policy)
