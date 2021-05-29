""" Contains utility functions for running Direct Utility Estimation """

import random


def sample_action(action):
    # sample random action given policy
    # (80% following policy,
    # 20% to left or right of policy)
    # create action pool
    if action == 'UP':
        action_pool = ['UP']*8 + ['LEFT'] + ['RIGHT']
    elif action == 'DOWN':
        action_pool = ['DOWN']*8 + ['RIGHT'] + ['LEFT']
    elif action == 'RIGHT':
        action_pool = ['RIGHT']*8 + ['UP'] + ['DOWN']
    else:
        action_pool = ['LEFT']*8 + ['DOWN'] + ['UP']
    # sample uniformly from action pool
    return random.choice(action_pool)


def get_next_state(grid, cur_state, action):
    # apply action to get next state (cell)
    # get next state based on action
    if action == 'UP':
        next_state = (cur_state[0]-1, cur_state[1])
    elif action == 'DOWN':
        next_state = (cur_state[0]+1, cur_state[1])
    elif action == 'RIGHT':
        next_state = (cur_state[0], cur_state[1]+1)
    else:
        next_state = (cur_state[0], cur_state[1]-1)
    # check whether next state is in grid
    if next_state[0] in range(0, grid.shape[0]) and next_state[1] in range(0, grid.shape[1]):
        # check whether next state reward is none (state is blocked)
        if grid[next_state]:
            return next_state
    # return the same current state (action failed)
    return cur_state


def perform_single_trial(grid, terminals, policy):
    # run a single random trial through the grid world
    # pick a random initial state
    x_dim = grid.shape[0]
    y_dim = grid.shape[1]
    while True:
        cur_state = (random.randint(0, x_dim-1), random.randint(0, y_dim-1))
        if grid[cur_state] and cur_state not in terminals:
            break
    # loop until terminal state is reached
    U = list()
    U.append([cur_state, grid[cur_state]])
    while True:
        # pick a random action (80% following policy,
        # 20% to left or right of policy)
        action = sample_action(policy[cur_state[0]][cur_state[1]])
        # apply action
        cur_state = get_next_state(grid, cur_state, action)
        # add reward of current state to utilities of all visited states
        for idx in range(len(U)):
            U[idx][1] += grid[cur_state]
        # add current state to list of visited states
        U.append([cur_state, grid[cur_state]])
        # check if terminal state is reached
        if cur_state in terminals:
            break
    # return estimated utilities
    return U
