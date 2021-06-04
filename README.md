# Grid World with Reinforcement Learning

A college project for _Machine Intelligence_ course. Exploring __Reinforcement Learning__ using __Direct Utility Estimation__ on grid world.

## Description

-   __Direct Utility Estimation__ on _three_ scenarios of grid world problem (_4X3_, _10X10_ with different final reward positions).

-   _Two_ types of __Direct Utility Estimation__ are considered :
    -   Using tabular representation.
    -   Using simple function approximator (shown in equation _21.10_ in reference).

## Usage

-   Update policies within text files in `policies` folder. Text files are named after the numbers of the corresponding grid worlds.

-   Run the direct utility estimation (using a specific representation on a specific grid) :
    ```bash
    python run.py <agent_number> <grid_number> <path/to/policy/text/file>
    ```
