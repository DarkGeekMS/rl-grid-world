""" Solves Direct Utility Estimation (DUE) Using Function Approximation (FA) """

import random
from utils import perform_single_trial


# define constants
LR = 0.001
TRIALS_COUNT = 10000


def update_params(trial_results, prev_params):
    # update function approximator parameters using gradient descent
    # initialize set of next parameters (thetas)
    next_params = list(prev_params)
    # run gradient descent for each state reward in trial
    # given in the format of : [ [ (y, x), REWARD ], ... ]
    for cell in trial_results:
        # compute predicted utility of cell
        pred_util = next_params[0] + next_params[1] * cell[0][1] + next_params[2] * cell[0][0]
        # update first parameter (theta0)
        next_params[0] = next_params[0] + LR * (cell[1] - pred_util)
        # update second parameter (theta1)
        next_params[1] = next_params[1] + LR * (cell[1] - pred_util) * cell[0][1]
        # update third parameter (theta2)
        next_params[2] = next_params[2] + LR * (cell[1] - pred_util) * cell[0][0]
    # return set of next parameters
    return next_params


def solve_fa(grid, terminals, policy):
    # solve direct utility estimation using function approximation
    # randomly initialize parameters list (uniform)
    params_set = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    # loop for a large number of trials
    for trial in range(TRIALS_COUNT):
        # perform a single trial
        U = perform_single_trial(grid, terminals, policy)
        # update parameters using gradient descent
        params_set = update_params(U, params_set)
    # print out estimated function parameters
    print("### Function Parameters ###")
    print("theta_0 = ", params_set[0])
    print("theta_1 = ", params_set[1])
    print("theta_2 = ", params_set[2])
    # print out estimated utilities
    print("\n### Estimated Utilities ###")
    for y in range(grid.shape[0]):
        row = ""
        for x in range(grid.shape[1]):
            if grid[y, x]:
                util = params_set[0] + x * params_set[1] + y * params_set[2]
                row += (str(round(util, 3)) + " ")
            else:
                row += "None "
        print(row)
