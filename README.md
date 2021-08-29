# NUSMV GRID GAME CONTROLLER SYNTHESIS

This is the Python repository about the Formal Methods in Software Development Project 2019/2020 in the Computer Science Master's Degree course of La Sapienza University of Rome.



## Goal Description ##

We developed a tool to synthesise a software controller for a given game map. The game map consists of a game grid with empty cells, cells containing obstacles, and a goal cell to be reached. The controller must be able to bring a player, from any initial cell to the goal cell. Such a player will perform a sequence of actions, by crossing several cells, up to reach the goal. It can only cross the empty cell. 

The tool uses NuSMV as a black-box to obtain the solution of a specific instance of that game. We can see an instance as a player that has to reach the goal cell by starting from a specific initial cell. Since the controller is defined on the whole grid, the tool uses NuSVM for NxM instances (as a worst case), where N and M are the dimensions of the grid. 

To do that, firstly, it generates a NuSMV model and then appropriately exploits the model checker's output. This procedure is repeated for every instance, *i.e.*, for every cell of the grid. 

NuSMV is one of the best existing known and most efficient model checkers. In this context, we used it not for verification but for synthesis purposes. 

In the Model Checking, a specific property (specification) can be verified by exploring the LTS that models the system states. In the case of a violation of that specification, the model checker returns a counterexample. Using an artificial intelligence technique called *planning*, we exploited the counterexample to get the solution of the modelled problem. In particular, the verifier checks the negation of a given specification in order to returns a counterexample (the minimum path) when the specification is satisfied. In this way, the controller can learn, for every cell, the correct action that brings to the goal. We modelled the specification through a specific class of temporal logic (*i.e.*, as an LTL specification).

We defined an action as *legal* as follows: 

- An action is legal if it brings the current state into a successor state, so the cell in which we move, in the neighbourhood of the current state, and the successor does not have an obstacle.

We defined an action as *correct* as follows:

- An action is correct if it is legal and if, from the current state, it is an optimal action that leads to the goal.


The counterexample gives us the sequence of states-actions (*i.e.*, a sequence of correct actions) to get from the current starting cell to the goal cell. By extracting this sequence starting from every cell, the controller is able to tell us if an action for a given state is correct or not. 

Since the model checker provides the minimum path, a correct action is also the optimal one.

The tool returns the Python code that contains a *K function*, *i.e.*, the software controller (as in [[1]](#1)). For every state in the controller (called *controllable state*), it tells us what are the actions that bring to the goal.  This means that a state is controllable if and only presents at least one path to the goal. *K* returns true if the given action is correct for the given state, false otherwise. In addition, the tool also returns the Python code of a function called *Legal* which returns true or false for each state if and only if a given action is legal for that given state. Both functions take a state and an action as input and return a boolean value.

Two algorithms have been implemented to generate the controller:

- A naive algorithm (standard algorithm) that checks, for each cell, if there is at least one path that brings to the goal. If it exists, NuSMV returns the counterexample.
- An optimised algorithm that takes into account some considerations:
  	1. If a cell contains an obstacle, it certainly will not have at least one path to the goal.
	2. If a cell is inside another optimal path, it will have a path up to the goal, and we do not need to interrogate NuSMV about that cell.

The optimised synthesis algorithm brings significant improvements in terms of the number of cells processed and execution time (it performs the synthesis in about half the time).

All the necessary mathematical definitions (controller, set of controllable states, LTS, control problem ..) come from [[1]](#1).

More informations are in this [presentation](doc/nusmv_controller_synthesis.pdf)


Only a few test cases have been updated. For the other test cases explained in the presentation, contact me.


## Input File ##

You can specify two types of input files.


The first type of input file is as follows:

```
Goal: (2, 2)
M: 3
N: 3
Grid: 
      0 1 1
      1 0 0 
      1 1 0
```

In this case, the file contains the goal cell, the grid size and the grid itself. You have a fixed grid. We used 1 to encode an obstacle and 0 to encode an empty cell. It is not possible to specify a goal cell that contains an obstacle.


The second type of input file is as follows:

```
Goal: (2, 2)
M: 3
N: 3
```

In this case, the file contains only the goal cell and the grid size. In such a context, the tool randomly generates a grid. The specified goal cell will not contain an obstacle.




## Additional Feature ##

An additional feature has been developed to check if there is at least one path to the goal from a given initial cell. The principle is always to query NuSMV as a black-box; it is not queried on the whole grid but only on the initial cell.

The input in this case has the form:

```
Goal: (6, 1)
Init: (2, 6)
N: 7
M: 7
Grid: 
      0 1 1 0 0 1 1 
      1 0 0 1 1 0 1 
      0 1 0 1 0 0 0 
      0 0 1 0 0 1 1 
      0 0 1 1 1 0 0 
      1 0 1 1 0 1 0 
      1 0 1 1 0 1 0
```

or

```
Goal: (6, 1)
Init: (2, 6)
N: 7
M: 7
```

If the grid is not specified, the tool  randomly generates it.




## Description and Requirements ##

Python 3 was used for the development of the tool. We developed and performed the experiments using Python 3.6 and Python 3.7 on Linux Systems. In particular, Linux Mint and Ubuntu.

The synthesis can be perfrmed by running the python file *main.py* as follows:

```
python main.py -conf config.ini -o output_folder input_file.input 
```

Through the `-o output_folder` option, you can specify the path of the output folder, i.e., the directory where the tool has to store the code of the controller.

The tool needs a path for  NuSMV executable (the tool uses the NuSMV binary executable file and the compilation is not foreseen) and a path to store NuSMV models. This informations can be specified in the `config.ini`.

Using the `-nogrid` option, the specified grid is not considered. It is required when the user specifies the non-grid input file. By default, the optimised synthesis algorithm is used. In any case, you can use `-mode 0` for the standard algorithm and `-mode 1` for the optimised algorithm. 

Using `-v 1`, you can increase the verbosity of the output. Using only the `-h` option, you get a summary of the available options.

For the other feature, which excludes the generation of the controller, the following syntax is used:

```
python main.py -path -conf config.ini input_file.input
```

In this case, no output code is generated, so it is not necessary to specify an output path.



The config.ini file must be defined as follows

```
[NUSMV]
nusmv=nusmv_executable_path

[MODEL]
nusmv_model_folder=nusmv_models_path
```

The tool uses the standard Python 3 libraries, along with the following additional libraries:

- psutils
- resource


NuSMV executable was not updated. This [file](nusmv/Readme.md) explains how to download it to run the code.


## References ##

<a id="1">[1]</a>
Mari, F., Melatti, I., Salvo, I., & Tronci, E. (2014). Model-based synthesis of control software from system-level formal specifications. ACM Transactions on Software Engineering and Methodology (TOSEM), 23(1), 1-42.



## License ##

The license for this software is: GPLv3. 





