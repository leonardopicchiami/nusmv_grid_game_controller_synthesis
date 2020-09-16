# NUSMV GRID GAME CONTROLLER SYNTHESIS

This is the Python repository about the Formal Methods in Software Development Project 2019/2020 in the Computer Science Master's Degree course of La Sapienza University of Rome.



## Goal Description ##

The goal of the system is to synthesize a controller for a given game map. The game map consists of a game grid with empty cells and cells containing obstacles and a given cell which is the goal cell to be reached. The system uses nusmv as a blackbox, generating a fixed NuSMV model type (one model for each cell of the grid assuming to start from that cell to reach the goal), interrogating NuSMV and appropriately exploiting the output obtained.

NuSMV is one of the best known and most efficient model checkers. In this case, it is not used for verification, but rather for synthesis. In model checking, assuming that a specific date is valid in each state of the system, LTS is passed and controlled. In case the specification is violated, a counterexample is returned. This property has been exploited using an artificial intelligence technique called planning, where the specification (certainly true) is negated in order to be surely violated. In this way the model checker will provide us with the solution we are looking for. The specification is also modeled through a specific class of logic called temporal logic.