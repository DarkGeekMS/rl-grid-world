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

## Assignment 4

-   Document : [Selected Papers Summary](https://docs.google.com/document/d/1huFa2wKRn6V-K3fm3VJpNsxcoUnh19sNAXTix1c-SzU/edit?usp=sharing)

-   Selected Papers :
    -   [Discovering Reinforcement Learning Algorithms](https://proceedings.neurips.cc/paper/2020/file/0b96d81f0494fde5428c7aea243c9157-Paper.pdf), DeepMind, NeurIPS 2020

    -   [Robust Multi-Agent Reinforcement Learning with Model Uncertainty](https://proceedings.neurips.cc/paper/2020/file/774412967f19ea61d448977ad9749078-Paper.pdf), AWS, NeurIPS 2020
