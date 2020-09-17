###########################################################################################################################
#                                                                                                                         #
# FileName    [controller.py]                                                                                             #
#                                                                                                                         #
# PackageName [controller]                                                                                                #
#                                                                                                                         #
# Synopsis    [This file contains the class that synthesize the controller and generates the controller Python code.      # 
#              It allows to generate the controller through the synthesis algorithm and generat a Python file to use and  #  
#              interrogate the controller. The controller is defined on a set of states (cells)                           #
#              that have at least one path up to the goal and by the (mathematical) function that defines                 #
#              the controller.]                                                                                           #
#                                                                                                                         #
# Author      [Leonardo Picchiami]                                                                                        #
#                                                                                                                         #
###########################################################################################################################



import parsing.model_checker_parsing as nusmv_pars
import model_synthesis.model_synthesis as mod
import code_generation.pycode_generator as pycode
import utils.utils as ut



class Controller(object):
    '''
    Class that synthesize the controller and generates the controller Python code.    
    It allows to generate the controller through the synthesis algorithm and generate a Python file to use and 
    interrogate the controller. The controller is defined on a set of states (cells)                       
    that have at least one path up to the goal and by the (mathematical) function that defines the controller.
    
    Attributes
    ----------
    grid : matrix of int
       It is a NxM matrix of integers where each cell can have the following values:
          - 0  if the cell has no obstacles.
          - 1  if the cell has an obstacles.
          - 2  if the cell is crossed during the verification.

    goal : tuple of int
       Coordinates of the goal cell.

    nusmv_path : string
       Path of the NuSMV model checker executable file.

    model_path : string
       Path of the folder which will contain the NuSMV models.

    controlled_states : list
       List of coordinates, i.e. cells, where there is a path from each cell to the goal.

    checked_cells : int
       Number of grid cells processed during verification.

    output_path : string
       Path of the generated code.
    '''

    
    def __init__(self, grid, goal, nusmv_path, model_path, output_path):
        '''
        Parameters
        ----------
        grid : matrix of int
           Starting game grid, where the values within it are either 0 or 1.

        goal : tuple of int 
           Coordinates of the goal cell.

        nusmv_path : string
           Path of the NuSMV model checker executable file.

        model_path : string
           Path of the folder which will contain the NuSMV models.

        output_path : string
           Path of the generated code.
        '''
        
        self.__grid = grid
        self.__goal = goal
        self.__nusmv_path = nusmv_path
        self.__model_path = model_path
        self.__output_path = output_path
        self.__checked_cells = 0
        self.__controlled_states = []




    def code_generation(self, states_actions_set):
        '''
        Generate the Python code of the Legal and K functions in an output Python file using the output of NuSMV.

        Parameters
        ----------
        states_actions_set : set
            The set that contains the state-correct_action pair, i.e. a state and the correct action for that state that leads on the right path to the goal
        '''
        
        code_generator = pycode.PyCodeGenerator(self.__output_path, "synthesis.py")
        code_generator.start()
        code_generator.write_Legal_function(self.__grid, self.__goal)
        code_generator.write_K_function(states_actions_set, len(self.__grid), len(self.__grid[0]))
        code_generator.close_file()

        
        
    def controller_synthesis(self):
        '''
        Generate the controller for the grid, i.e. generate the list of all coordinates that have at least one path leading to the target and the Python code 
        of the K function (and the Legal function for comparison) so that you can use it if a pair action-state is controllable.
        This version is the basic algorithm that checks all cells and looks if there is a counterexample returned by NuSMV, 
        if there is a path leading to the target and therefore the cell will be added to the set of controlled states and will be enabled to the controller 
        the correct action leading to the goal.
        '''
    
        N = len(self.__grid)
        M = len(self.__grid[0])

        states_actions = set()
        for i in range(N):
            for j in range(M):
                self.__checked_cells += 1
                model_path = self.__model_path
                model_path += "model_{0}x{1}-{2}_{3}.smv".format(N, M, i, j)
                ut.nusmv_model_synthesis(N, M, self.__grid, (i, j), self.__goal, model_path)
                
                checker_res = ut.nusmv_subroutine(self.__nusmv_path, model_path, (i, j))
                
                nusmv_parser = nusmv_pars.ModelCheckerParsing(checker_res)
                if nusmv_parser.exists_path_init_to_goal(self.__goal):
                    self.__controlled_states.append((i, j))
                    nusmv_parser.parse_state_action_conterexample()

                    s_a = nusmv_parser.get_correct_state_action()
                    if s_a:
                        states_actions.add(s_a)

                    
        if len(self.__controlled_states) > 0:
            self.code_generation(states_actions)

        else:
            print("\n\nThe controller cannot be generated, there have been no states for which no action can be enabled.\n\n")


            
    def optimized_controller_synthesis(self):
        '''
        Generate the controller for the grid, i.e. generate the list of all coordinates that have at least one path leading to the target and the Python code 
        of the K function (and the Legal function for comparison) so that you can use it if a pair action-state is controllable.
        This version is optimized: it only considers the cells that do not have an obstacle and parses the cells crossed 
        to reach the goal indicated by the counterexample. The assumption is used that if a cell is crossed to reach the goal, 
        it itself has a path that leads to the goal. This reduces the cells in which the path is explicitly checked.
        '''
        
        N = len(self.__grid)
        M = len(self.__grid[0])

        states_actions = set()
        for i in range(N):
            for j in range(M):
                if (i, j) not in self.__controlled_states and self.__grid[i][j] == 0:
                    self.__checked_cells += 1
                    model_path = str(self.__model_path)
                    model_path += "model_{0}x{1}-{2}_{3}.smv".format(N, M, i, j)
                    ut.nusmv_model_synthesis(N, M, self.__grid, (i, j), self.__goal, model_path)

                    checker_res = ut.nusmv_subroutine(self.__nusmv_path, model_path, (i, j))
                    
                    nusmv_parser = nusmv_pars.ModelCheckerParsing(checker_res)
 
                    if nusmv_parser.exists_path_init_to_goal(self.__goal):
                        nusmv_parser.parse_state_action_conterexample()
                        states_actions |= set(nusmv_parser.get_postprocessed_state_action())
                        
                        for cell in nusmv_parser.get_crossed_states():
                            if not cell in self.__controlled_states:
                                self.__controlled_states.append(cell)

        
        if len(self.__controlled_states) > 0:
            self.code_generation(states_actions)
  
        else:
            print("\n\nThe controller cannot be generated, there have been no states for which no action can be enabled.\n\n")
                    
        
                                
    def get_controlled_states(self):
        '''
        Returns the controllable states, i.e. the set of cells that have at least one path up to the goal.

        Returns
        -------
        controller : list
           List of coordinates, i.e. cells, where there is a path from each cell to the goal.
        '''
        
        return self.__controlled_states


    
    def get_number_checked_cells(self):
        '''
        Returns the number of grid cells processed during verification.

        Returns
        -------
        checked_cells : int
           Number of grid cells processed during verification.
        '''
        
        return self.__checked_cells
