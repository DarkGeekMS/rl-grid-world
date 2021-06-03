""" Solves Direct Utility Estimation (DUE) Using Tabular Representation """

import numpy as np
from utils import perform_single_trial


# define constants
TRIALS_COUNT = 10000


def summarize_trial(trial_results):
    # summarize the trial results by collecting similar cells together
    # loop over each cell in trial results
    trial_stats = dict()
    for cell in trial_results:
        # store summation of utilities and number of occurances
        # for each cell in trial results
        if cell[0] in trial_stats.keys():
            trial_stats[cell[0]][0] += cell[1]
            trial_stats[cell[0]][1] += 1
        else:
            trial_stats[cell[0]] = [cell[1], 1]
    # calculate mean of each cell from trial statistics
    sum_trial_results = list()
    for cell in trial_stats.keys():
        # calculate cell mean
        cell_mean = trial_stats[cell][0] / trial_stats[cell][1]
        sum_trial_results.append([cell, cell_mean])
    # return summarized trial results
    return sum_trial_results


def update_util_table(trial_results, util_table):
    # update utility table with trials results
    # loop over each cell in trail results
    # given in the format of : [ [ (y, x), REWARD ], ... ]
    for cell in trial_results:
        # update cell in utility table
        if util_table[cell[0]]:
            # if not None, with average of existing utility and trial outcome
            util_table[cell[0]] = (util_table[cell[0]] + cell[1]) / 2.0
        else:
            # if none, with trial outcome
            util_table[cell[0]] = cell[1]
    # return next utility table
    return util_table


def solve_tabular(grid, terminals, policy):
    # solve direct utility estimation using tabular representation
    # intialize whole utility table with None
    util_table = np.full(grid.shape,  None)
    # loop for a large number of trials
    for trial in range(TRIALS_COUNT):
        # perform a single trial
        U = perform_single_trial(grid, terminals, policy)
        # summarize trial results
        U2 = summarize_trial(U)
        # update utility table
        util_table = update_util_table(U2, util_table)
    # print estimated utility table
    print("### Estimated Utilities Table ###")
    for y in range(util_table.shape[0]):
        row = ""
        for x in range(util_table.shape[1]):
            if util_table[y, x]:
                row += str(round(util_table[y, x], 3)) + " "
            else:
                row += "None "
        print(row)
