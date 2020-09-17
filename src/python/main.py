######################################################################################################################################
#                                                                                                                                    #
# FileName    [main.py]                                                                                                              #
#                                                                                                                                    #
# PackageName [main]                                                                                                                 #
#                                                                                                                                    #
# Syopsis     [Python script that represents the main of the program.                                                                #
#              Generate the grid controller: generate the Python code of the K function which returns True if the input action       #
#              is the right action that leads to the goal cell. The set of states that have a path up to the goal is defined,        #
#              that is, the set of controllable states. The states for which the controller has enabled actions belong to this set.  #
#              There are two versions of the controller generation algorithms: one optimized and one standard.                       #
#              Also, after choosing an init cell, it allows you to check if there is a path from the init cell to the target cell    #
#              without generating the controller.                                                                                    #
#                                                                                                                                    # 
# Author      [Leonardo Picchiami]                                                                                                   #
#                                                                                                                                    #
######################################################################################################################################



import argparse as arg
import sys
import configparser as cfg
import time, os, psutil
import resource as res


import controller.controller as ctrl
import model_synthesis.model_synthesis as mod
import parsing.model_checker_parsing as nusmv_pars
import parsing.input_parsing as input_pars
import utils.utils as ut


def exists_path_algorithm(grid, init, goal, nusmv_path, nusmv_model_folder):
    '''
    Check that there is at least one path from the init cell to the goal cell.

    Parameters
    ----------
    grid : matrix of int
       Starting game grid, where the values within it are either 0 or 1.

    init : tuple of int
       Coordinates of the init cell.

    goal : tuple of int
           Coordinates of the goal cell.

    nusmv_path : string
       Path of the NuSMV executable file.

    model_path : string
       Path of the NuSMV model file. 
    '''
    
    N = len(grid)
    M = len(grid[0])

    model_path = str(nusmv_model_folder)
    model_path += "model_{0}x{1}-init{2}_{3}-goal{4}_{5}.smv".format(N, M, init[0], init[1], goal[0], goal[1])
    ut.nusmv_model_synthesis(N, M, grid, init, goal, model_path)
    
    checker_res = ut.nusmv_subroutine(nusmv_path, model_path, init)
    nusmv_parser = nusmv_pars.ModelCheckerParsing(checker_res)
    
    if  nusmv_parser.exists_path_init_to_goal(goal):
        print("\n\nThere is at least one path from init ({0}, {1}) to goal ({2}, {3})".format(init[0], init[1], goal[0], goal[1]))

    else:
        print("\n\nThere is no path init ({0}, {1}) to goal ({2}, {3})".format(init[0], init[1], goal[0], goal[1]))

        
        
def controller_synthesis_algorithm(mode, grid, goal, nusmv_path, nusmv_model_folder, output_path_folder):
    '''
    Generate a grid controller using the selected algorithm.

    Return an instance of the controller class. This instance represents the generated controller. 
    So the set of states that have at least one path up to the goal was generated; that is, it allows to use the function K
    which returns true if a state-action pair is lawful (the state must be a controllable state, therefore it must be in the set of states calculated).

    Parameters
    ----------
    mode : int
       Controller synthesis selected algorithm:
       - 0 standard algorithm
       - 1 optimized algorithm

    grid : matrix of int
       Starting game grid, where the values within it are either 0 or 1.

    goal : tuple of int
           Coordinates of the goal cell.

    nusmv_path : string
       Path of the NuSMV executable file.

    model_path : string
       Path of the NuSMV model file.


    Returns
    -------
    controller : Controller
       The instance of the grid controller.
       
    '''
    
    controller = ctrl.Controller(grid, goal, nusmv_path, nusmv_model_folder, output_path_folder)
    
    if mode == 0:
         controller.controller_synthesis()

    if mode == 1:
        controller.optimized_controller_synthesis()


    return controller


    
def main():
    '''
    Main function that manages the system.
    '''
    parser = arg.ArgumentParser("Main argument parser.", conflict_handler = 'resolve')

    #Optional agument: options of the program
    parser.add_argument('-conf' , action = 'store', dest = 'conf_file', help = "Path of config file. Path of the configuration file. By default it is in the main folder")
    parser.add_argument('-nogrid', action = 'store_true', dest = 'no_grid', help = "Excluding the grid from parsing the input file.")
    parser.add_argument('-path', action = 'store_true', dest = 'path', help = "Check if there is a path from the start to the goal.")
    parser.add_argument('-mode', action = 'store', dest = 'mode', help = "Select the controller synthesis algoithm: 0 standard, 1 optimized (default).")
    parser.add_argument('-v', action = 'store', dest = 'v', help = "Level of verbosity. 0 is current level, 1 is max level of verbosity.")
    parser.add_argument('-o ', action = 'store', dest = 'out_path', help = "Path of output file.")
    
    #Mandatory argument: input file path
    parser.add_argument('input', action = 'store', help = "Path of input file.")
    

    results = parser.parse_args()


    
    #Configuration settings and parsing
    config_file = "config.ini"    
    if results.conf_file:
       config_file = results.conf_file 
    
    config_parser = cfg.ConfigParser()
    config_parser.read(config_file)


    if results.path and results.out_path:
        parser.error("You cannot define an output destination without generating the controller.")

        
    #Configuration settings and parsing
    input_parser = input_pars.InputParser()

    if results.no_grid:
        input_parser.file_nogrid_parser(results.input, results.path)
    else:
        input_parser.file_grid_parser(results.input, results.path)

    

    if results.path and results.mode:
        parser.error("You decide to check if exits almost one path fro init to goal. You must not specify modality of controller generation.")



    #NuSMV model folder path correctness control
    nusmv_model_folder = config_parser['MODEL']['nusmv_model_folder']
    if nusmv_model_folder[-1] != '/':
        nusmv_model_folder += '/'


    #Controller synthesis algorithm selection     
    controller_mode = [0, 1]
    mode = 1
    if results.mode and int(results.mode) == 0:
        mode = int(results.mode)

    if results.mode and (int(results.mode) not in controller_mode):
        parser.error("The option to choose the controller generation algorithm is not in [0, 1].")


    #Verbosity setting control
    if results.v and (int(results.v) > 1 or int(results.v) < 0):
        parser.error("There is no such high level of verbosity or the value is negative.")


        
    print("********************** NUSMV GAME GRID CONTROLLER SYNTHESIS ***********************\n\n")
    print("Number of line N: {0}".format(input_parser.get_n()))
    print("Number of column M: {0}".format(input_parser.get_m()))

    
    if results.path:
        print("Init of the grid: {0}".format(input_parser.get_init()))

    print("Goal of the grid: {0}".format(input_parser.get_goal()))

    print("\n\nGrid value 0: grid cell without obstacle (traversable cell).")
    print("Grid value 1: grid cell with obstacle.")

    
    if results.v and int(results.v) == 1 and not results.path:
        print("Grid value 2: controlled grid cell.")

        
    if results.path:
        print("Grid value I: init cell")
              
    print("Grid value G: goal cell.")

              
    print("\n\nGame grid: \n")
    ut.print_grid(input_parser.get_n(), input_parser.get_m(), input_parser.get_grid(), input_parser.get_goal(), results.path, input_parser.get_init())

    
    
    if results.path:
        exists_path_algorithm(input_parser.get_grid(), input_parser.get_init(), input_parser.get_goal(), config_parser['NUSMV']['nusmv'], nusmv_model_folder)

    else:

        if not results.out_path:
            parser.error("To generate a controller you must give the output path for the controllore code.")
            
        output_path_folder = results.out_path

        start_time = time.time()
                
        controller = controller_synthesis_algorithm(mode, input_parser.get_grid(), input_parser.get_goal(), config_parser['NUSMV']['nusmv'], nusmv_model_folder, output_path_folder)
        
        
        #Execution time of controller synthesis
        execution_time = time.time() - start_time

        
        if mode == 0:
            print("\n\nController synthesis algorithm: standard.")
        if mode == 1:
            print("\n\nController synthesis algorithm: optimized.")

        

        if results.v and int(results.v) == 1:
            ut.verbosity(input_parser.get_n(), input_parser.get_m(), input_parser.get_grid(), input_parser.get_goal(), controller.get_controlled_states())

        if len(controller.get_controlled_states()) > 0:
            print("\n\nControlled states of generated controller:\n")
            print(controller.get_controlled_states())

        else:
            print("\n\nThere are no controllable states:\n")
            print(controller.get_controllable_states())
            

        
        print("\n\n\n***** STATISTICS *****\n")
        empty = ut.empty_cells(input_parser.get_n(), input_parser.get_m(), input_parser.get_grid())
        
        print("Empty cells: {0}.".format(empty))
        print("Cells with obstacles: {0}".format(input_parser.get_n() * input_parser.get_m() - empty))
        print("Controllable cells: {0}.".format(len(controller.get_controlled_states())))
        print("Processed cells: {0}.\n".format(controller.get_number_checked_cells()))

        ut.display_execution_time(execution_time)

        process = psutil.Process(os.getpid())
        
        ut.display_memory_usage(process.memory_info().rss)

        
        

            
        
if __name__ == '__main__':
    main()
