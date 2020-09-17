#################################################################################################
#                                                                                               #
# FileName    [utils.py]                                                                        #
#                                                                                               #
# PackageName [utils]                                                                           #
#                                                                                               #
# Synopsis    [This file contains some useful functions.]                                       # 
#                                                                                               #
# Author      [Leonardo Picchiami]                                                              #
#                                                                                               #
#################################################################################################


import subprocess as sub
import model_synthesis.model_synthesis as mod
import random



def nusmv_subroutine(nusmv_path, model_path, cell):
    '''
    Invokes the NuSMV executable by giving it the model input and returns the output obtained from the model checker.

    Parameters
    ----------
    nusmv_path : string
       Path of the NuSMV executable file.

    model_path : string
       Path of the NuSMV model file.


    Returns
    -------
    res : string
       String that contains the output obtained from the model checker.

    '''

    #memory_cmd = "/usr/bin/time -v -o memory_log/subproc_memory_{0}_{1}.log".format(cell[0], cell[1])
    cmd = nusmv_path + " " + model_path
    res = sub.check_output(cmd, shell = True)
    return res



def nusmv_model_synthesis(N, M, grid, init, goal, model_path):
    '''
    Generate the NuSMV model and write it to file.

    Parameters
    ----------  
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.

    grid : matrix of int
       Starting game grid, where the values within it are either 0 or 1.
         
    init : tuple of int
       Coordinates of the init cell.
    
    goal : tuple of int
       Coordinates of the goal cell.

    model_path : string
       Path of NuSMV model.
    '''
    
    model_generator = mod.ModelSynthesis(grid, N, M, init, goal)
    model_generator.generate_model()

    with open(model_path, "w") as f:
        f.write(model_generator.get_model())

        

def print_grid(N, M, grid, goal, exist_path=False, init=None):
    '''
    Display the grid on the stdout.

    Parameters
    ----------
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.

    grid : matrix of int
       The game grid
    
    goal : tuple of int
       Coordinates of the goal cell.

    exist_path : boolean, optional
       Flag if it indicates that a path is being checked from a given init to the goal and the controller is not being generated.

    init : tuple fo int, optional
       Init cell of the grid.
    '''
    
    for i in range(N):
        for j in range(M):
            if exist_path and (i, j) == init:
                print("I" + " ", end = '')
            elif (i, j) == goal:
                print("G" + " ", end = '')
            else:
                print(str(grid[i][j]) + " ", end = '')

        print("\n", end = '')

        

def matrix_copy(N, M, grid):
    '''
    Copies the matrix (the grid) as input and returns the copy.

    Parameters
    ----------
    N : int
      Number of grid rows.

    M : int
       Number of grid columns.

    grid : matrix of int
       The game grid.

    
    Returns
    -------
    new_grid : matix of int
       The copied matrix (grid).
    '''
    
    new_grid = []
    for i in range(N):
        tmp_list = []
        for j in range(M):
            tmp_list.append(int(grid[i][j]))
            
        new_grid.append(tmp_list)

    return new_grid



def verbosity(N, M, grid, goal, controlled_states):
    '''
    Prints the controlled matrix, that is, assigns the value 2 to the cells of the grid crossed and displays the grid on the stdout.

    Parameters
    ----------
    N : int
      Number of grid rows.

    M : int
       Number of grid columns.

    grid : matrix of int
       The game grid.
    
    goal : tuple of int
       Coordinates of the goal cell.

    controlled_states : list
       List of coordinates, i.e. cells, where there is a path from each cell to the goal.
    '''
    
    tmp_grid = matrix_copy(N, M, grid)

    for cell in controlled_states:
        tmp_grid[cell[0]][cell[1]] = 2

    print("\n\n***** Controlled Grid *****\n\n")
    print_grid(N, M, tmp_grid, goal)


    

def empty_cells(N, M, grid):
    '''
    Returns the empty cell number of the input grid.

    Parameters
    ----------
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.

    grid : matrix of int
       The game grid.

    
    Returns
    -------
    count : int
       Calculed number of empty cell.
    '''
    
    count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                count += 1

    return count



def controlled_cells(N, M, grid, controlled_states):
    '''
    
    Parameters
    ----------
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.

    grid : matrix of int
       The game grid.

    controlled_states : list
       List of coordinates, i.e. cells, where there is a path from each cell to the goal.


    Returns
    -------
    count : int
       Calculed number of controlled cell.
    '''
    
    tmp_grid = matrix_copy(N, M, grid)

    for cell in controlled_states:
        tmp_grid[cell[0]][cell[1]] = 2

    count = 0
    for i in range(N):
        for j in range(M):
            if tmp_grid[i][j] == 2:
                count += 1

    return count



def cell_neighborhood(N, M, controlled_states, state):
    '''
    This function that calculates the neighborhood of a cell in the grid according to the controlled states, 
    i.e. the states that have at least one path up to the goal cell. This function indicates the possible cells 
    reachable from the current cell, or alternatively the set of successor states reachable from the current state.
    
    Parameters
    ----------
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.
    
    controlled_states : list
       List of coordinates, i.e. cells, where there is a path from each cell to the goal.

    state : tuple
       The cell (state) whose neighborhood is calculated.


    Returns
    -------
    neighborhood : list
        List of cells in the neighborhood of the input cell that have at least one path to the goal.
    '''
    
    neighborhood = []
    for i in range(state[0] - 1, state[0] + 2):
        for j in range(state[1] - 1, state[1] + 2):
            if i == state[0] and j == state[1]:
                continue
            
            if (i < 0 or i > N) or (j < 0 or j > M):
                continue

            if (i, j) in controlled_states:
                neighborhood.append((i, j))

    return neighborhood




def display_execution_time(execution_time):
    '''
    Function that prints to stdout, given the execution time in seconds, the equivalent in hours, minutes and seconds.

    Parameters
    ----------
    execution_time : float
        Execution time in seconds
    '''
    
    if execution_time < 60:
        print("Execution time: {0} sec.".format(execution_time))

    elif execution_time/60 < 60:
        min_exec_time = int(execution_time / 60)
        sec_exec_time = execution_time % 60
        print("Execution time: {0} sec".format(execution_time))
        print("Execution time: {0} min {1} sec.".format(min_exec_time, sec_exec_time))

    elif execution_time/3600 < 24:
        sec_exec_time = execution_time % 60
        tmp_exec_time = execution_time / 60
        min_exec_time = int(tmp_exec_time % 60)
        hour_exec_time = int(tmp_exec_time / 60)
        print("Execution time: {0} sec".format(execution_time))
        print("Execution time: {0} hour {1} min {2} sec.".format(hour_exec_time, min_exec_time, sec_exec_time))



def display_memory_usage(memory_usage):
    '''
    Function that prints to stdout, given the number of bytes that the process running the python application uses, the equivalent in KB, MB or GB. 

    Parameters
    ----------
    memory_usage : int
        Memory used in bytes
    '''
    
    if memory_usage < 2.**10:
        print("Python process RAM usage: {0} B".format(memory_usage))

    elif memory_usage/2**10 < 1024:
        print("Python process RAM usage: {0} KB".format(memory_usage/2**10))

    elif memory_usage/2**20 < 1024:
        print("Python process RAM usage: {0} MB".format(memory_usage/2**20))

    elif memory_usage/2**30 < 1024:
        print("Python process RAM usage: {0} GB".format(memory_usage/2**30))


        
def random_tests(N, M, controller, sequence_act):
    '''
    This function performs random tests on the generated controller. 
    Invoke the function K many times when the actions to be tested are returned and return true/false 
    if the state-action pair (therefore cell-action) is lawful or not. To be lawful, the cell must be in the calculated cell set.
    
    Parameters
    ----------
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.

    controller : Controller
       Instance of the Controller class representing the generated controller.

    sequence_act : list
       List of strings representing the set of actions to be tested on the controller.
    '''

    
    print("\n\n\n***** TEST CONTROLLER INTERROGATION *****\n")

    if len(controller.get_controlled_states()) == 0:
        print("\n\nThere is no controller for the given game grid.")
        print("Tests could not be performed by interrogating the controller.")
        exit(0)

   #  print("K(({0}, {1}), {2}) = {3}".format(4, 8, "right-up", controller.K((4, 8), "right-up")))
  #  print("K(({0}, {1}), {2}) = {3}\n".format(4, 8, "right", controller.K((4, 8), "right")))
   # print("K(({0}, {1}), {2}) = {3}".format(1, 0, "down", controller.K((1, 0), "down")))
    for index in range(len(sequence_act)):
        rand_i = random.randint(0, N-1)
        rand_j = random.randint(0, M-1)
        res = controller.K((rand_i, rand_j), sequence_act[index])
        print("K(({0}, {1}), {2}) = {3}".format(rand_i, rand_j, sequence_act[index], res))
        


        
def game_example_tests(N, M, controller):
    '''
    Ad-hoc tests designed to test the generated controller on the grid inserted in the presentation. 
    This grid is among the tests: test3x3game-goal2_2.

    Parameters
    ----------
    N : int
       Number of grid rows.

    M : int
       Number of grid columns.

    controller : Controller
       Instance of the Controller class representing the generated controller.
    '''
    
    print("\n\n\n***** TEST CONTROLLER INTERROGATION *****\n")

    if len(controller.get_controlled_states()) == 0:
        print("\n\nThere is no controller for the given game grid.")
        print("Tests could not be performed by interrogating the controller.")
        exit(0)

        
    print("K(({0}, {1}), {2}) = {3}".format(1, 2, "down", controller.K((1, 2), "down")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 2, "left", controller.K((1, 2), "left")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 1, "right-down", controller.K((1, 1), "right-down")))
    print("K(({0}, {1}), {2}) = {3}".format(1, 1, "right", controller.K((1, 1), "right")))
    print("K(({0}, {1}), {2}) = {3}".format(2, 0, "left-up", controller.K((2, 0), "left-up")))
    print("K(({0}, {1}), {2}) = {3}".format(0, 1, "left-down", controller.K((0, 1), "left-down")))
    print("K(({0}, {1}), {2}) = {3}".format(0, 0, "right-down", controller.K((0, 0), "right-down")))
    print("K(({0}, {1}), {2}) = {3}".format(2, 1, "up", controller.K((2, 1), "up")))  


