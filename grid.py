""" Generates the grid world MDP """

import numpy as np


def get_world_1():
    # form the first grid world
    # 4X3 grid with terminals at (4,3) +1
    # and at (4,2) -1
    grid = np.array(
        [[-0.04, -0.04, -0.04, +1],
        [-0.04, None, -0.04, -1],
        [-0.04, -0.04, -0.04, -0.04]]
    )
    terminals = [(0, 3), (1, 3)]
    return grid, terminals


def get_world_2():
    # form the second grid world
    # 10X10 grid with terminals at (10,10) +1
    grid = np.full((10, 10), -0.04)
    grid[0, 9] = +1
    terminals = [(0, 9)]
    return grid, terminals


def get_world_3():
    # form the third grid world
    # 10X10 grid with terminals at (5,5) +1
    grid = np.full((10, 10), -0.04)
    grid[4, 4] = +1
    terminals = [(4, 4)]
    return grid, terminals
