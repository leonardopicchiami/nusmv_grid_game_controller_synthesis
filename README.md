# NUSMV GRID GAME CONTROLLER SYNTHESIS

This is the Python repository about the Formal Methods in Software Development Project 2019/2020 in the Computer Science Master's Degree course of La Sapienza University of Rome.



## Goal Description ##

The goal of the system is to synthesize a controller for a given game map. The game map consists of a game grid with empty cells, cells containing obstacles and a given cell which is the goal cell to be reached. The system uses nusmv as a blackbox, generating a fixed NuSMV model type (one model for each cell of the grid assuming to start from that cell to reach the goal), interrogating NuSMV and appropriately exploiting the output obtained.

NuSMV is one of the best known and most efficient model checkers. In this case, it is not used for verification, but for synthesis. In model checking, a specific property (specification) is verified by visiting the LTS representing the system states. In case the specification is violated, a counterexample is returned. This property has been exploited using an artificial intelligence technique called *planning*, where a true specification is negated in order to abtain the solution for that problem. The specification is modeled through a specific class of logic called temporal logic (in this case, as a LTL specification).

The counterexample gives us the correct sequence of states-actions to get from the current starting cell to the goal cell. Being defined on the whole grid, if the cell does not have an obstacle the generated controller knows which is the correct action to get to the goal from each cell. Since the model checker provides the minimum path, the move is also the optimal one.

The system returns Python code containing a *K function* that contains all the correct actions from every controllable state, so from every state that has at least one path to the goal. So it returns true if the given action is correct for the given state, false otherwise. In addition, it also issues returns the Python code of a function called *Legal* which returns true or false for each state if and only if a given action is legal for that given state. Both functions take a state and an action as input and return a boolean value.

Two algorithms have been implemented that generate the controller:

- A naive algorithm (called standard algorithm) that checks, for each cell, if there is at least one path to the goal. If exists, the counterexample is returned.
- An optimized algorithm that takes into account some considerations:
   1. If a cell contains an obstacle, it certainly will not have at least one path to the goal.
   2. If a cell is inside another path, it will surely have a path up to the goal and therefore NuSMV will not interrogated about that cell.

The second synthesis algorithm brings significant improvements in terms of the number of cells processed and the execution time (it performs the synthesis in about half the time).

All the necessary mathematical definitions (controller, set of controllable states, LTS, control problem ..) come from [[1]](#1).

More informations are in this [presentation](doc/nusmv_controller_synthesis.pdf)


Only a few test cases have been reported. For the other test cases explained in the presentation please contact me.


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

In this case, the whole file is parsed obtaining the goal cell, the grid size and the grid itself. You have a fixed grid. With 1 the cell with obstacle is coded, with 0 the empty cell. Clearly it is not possible to specify a goal cell that contains an obstacle.


The second type of input file is as follows:

```
Goal: (2, 2)
M: 3
N: 3
```

In this case, parsing the file, we get the goal cell and the grid size. The grid is generated randomly with the constraint that the goal cell cannot have an obstacle.




## Additional Feature ##

An additional feature has been developed to check if there is at least one path to the goal from a given initial cell. The principle is always to query NuSMV as a blackbox; it is not queried on the whole grid but only on the initial cell.

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

In case the grid is not specified, it is generated randomly.




## Description and Requirements ##

Python 3 was used for the development of the system. The system was developed and tested on 64-bit Python 3.6 and 64-bit Python 3.7 on Linux Systems. It has been developed and tested on Linux distros: Linux Mint and Ubuntu. The synthesis can be done by executing the python file main.py with the following syntax:

```
python main.py -conf config.ini -o output_folder input_file.input 
```

With the `-o output_folder` option you specify the path of the output folder, i.e. the folder where the file with the generated python code is to be saved. The path of the NuSMV executable (the system uses the NuSMV binary executable file and the compilation is not foreseen) and the path where the NuSMV models generated used by the model checker are saved, are specified in the `config.ini`.

Using the `-nogrid` option, the specified grid is not considered. It is required when specifying the non-grid input file. By default the most efficient algorithm for synthesis is used, you can use `-mode 0` for the standard algorithm and `-mode 1` for the optimized agorithm. With `-v 1` increases the verbosity of the output. Using only the `-h` option, you get a summary of the available options.

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

The system uses the standard Python 3 libraries, along with the following additional libraries:

- psutils
- resource


NuSMV executable was not loaded. NuSMV executable was not loaded. This [file](nusmv/Readme.md) explains how to download it to run the code.


## References ##

<a id="1">[1]</a>
Mari, Federico & Melatti, Igor & Salvo, Ivano. (2011). Model Based Synthesis of Control Software from System Level Formal Specifications. ACM Transactions on Software Engineering and Methodology. 23. 10.1145/2559934.



## License ##

The license for this software is: GPLv3. 





