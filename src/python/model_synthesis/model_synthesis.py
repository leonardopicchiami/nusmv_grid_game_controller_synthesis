###################################################################################################################################
#                                                                                                                                 #
# FileName    [model_synthesis.py]                                                                                                #
#                                                                                                                                 #
# PackageName [model_synthesis]                                                                                                   #
#                                                                                                                                 #
# Synopsis    [This file contains the class that dynamically generates the NuSMV model in order to verify the specifications.     #
#              The DEFINE section  allows you to define global macros that are not included in the state space,                   #
#              the VAR section is defined which constitutes the state space,                                                      #
#              the ASSIGN section where the set of initial states and transition relationship                                     #
#              and the LTL specification are defined.]                                                                            #
#                                                                                                                                 #
# Author      [Leonardo Picchiami]                                                                                                #
#                                                                                                                                 #
###################################################################################################################################




class ModelSynthesis(object):
    '''
    Class that dynamically generates the NuSMV model in order to verify the specifications.
    The DEFINE section allows you to define global macros that are not included in the state space,
    the VAR section is defined which constitutes the state space, 
    and the ASSIGN section where the set of initial states and transition relationship and the LTL specification are defined are defined.

    Attributes
    ----------
    n : int
       Number of grid rows.

    m : int
       Number of grid columns.

    grid : matrix of int
       It is a NxM matrix of integers where each cell can have the following values:
          - 0  if the cell has no obstacles.
          - 1  if the cell has an obstacles.
          - 2  if the cell is crossed during the verification.

    init : tuple of int
       Coordinates of the init cell.
    
    goal : tuple of int
       Coordinates of the goal cell.
    '''


    def __init__(self, grid, N, M, init, goal):
        '''
        Parameters
        ----------
        grid : matrix of int
           Starting game grid, where the values within it are either 0 or 1.
        
        N : int
           Number of grid rows.

        M : int
           Number of grid columns.
        
        
        init : tuple of int
           Coordinates of the init cell.
    
        goal : tuple of int
           Coordinates of the goal cell.

        '''

        self.__n = N
        self.__m = M
        self.__grid = grid
        self.__init = init
        self.__goal = goal
        self.__model = ""
        
        

    def generate_model(self):
        '''
        Generate the complete NuSMV model to verifying the existence of at least one path from the init cell to the goal cell.
        '''
        
        self.__model += "MODULE main\n\n"
        self.__model += self.generate_not_state_space_components()
        self.__model += self.generate_state_space()
        self.__model += self.generate_transition_relation()
        self.__model += self.generate_ltl_specification()



    def generate_not_state_space_components(self):
        '''
        Generates the DEFINE section of the NuSMV model and adds the macro macros to the model that are not included in the state space.

        Returns
        -------
        model_define : string
            String that contains the DEFINE section of the model.
        '''
        
        model_define = "  DEFINE\n\n"
        model_define += "     grid := {0};\n".format(self.__grid)
        model_define += "     N := {0};\n".format(self.__n)
        model_define += "     M := {0};\n\n\n".format(self.__m)
        return model_define
        
        


        
    def generate_state_space(self):
        '''
        Generates the definition of the state space, therefore of the variables, of the NuSMV model (VAR section).

        Returns
        -------
        model_variables : string
           String that contains the definition the state space, therefore of the variables, of the NuSMV model.
        '''
        
        model_variables = "  VAR\n\n"
        model_variables += "     i : 0..{0};\n".format(self.__n-1)
        model_variables += "     j : 0..{0};\n".format(self.__m-1)
        model_variables += "     action : {no-action, up, right-up, left-up, down, right-down, left-down, left, right};\n\n\n"
        return model_variables

    

    def generate_transition_relation(self):
        '''
        Generate all the definition of the initial states and the transition relationship of the NuSMV model by calling the appropriate subroutines.

        Returns
        -------
        model_assignments : string
           String that contains the definition of the initial states and the transition relationship of the NuSMV model.
        '''
        
        model_assignments = "  ASSIGN\n\n"
        model_assignments += self.generate_init_transition_relation()
        model_assignments += "\n\n"
        model_assignments += self.generate_next_transition_relation()
        return model_assignments


    
    def generate_init_transition_relation(self):
        '''
        Generates the definition of the set of initial states of the NuSMV model.

        Returns
        -------
        init_assignment : string
           String containing the definition of the set of initial states of the NuSMV model.
        '''
        
        init_assignment = "      init(i) := {0};\n".format(self.__init[0])
        init_assignment += "      init(j) := {0};\n".format(self.__init[1])
        init_assignment += "      init(action) := no-action;\n\n"
        
        return init_assignment

    

    def generate_next_transition_relation(self):
        '''
        Generates all transition relationship of the NuSMV model by calling the appropriate subroutines.
 
        Returns
        -------
        control : string
           String containing the definition of transition relationship of the NuSMV model.
        '''
        
        next_assignment = ""
        next_assignment += self.action_next_relation()
        next_assignment += self.i_coordinate_next_relation()
        next_assignment += self.j_coordinate_next_relation()
        
        return next_assignment

    
                
    def action_next_relation(self):
        '''
        Generates the definition of the transition relationship for the action variable.

        Returns
        -------
        action : string
            String containing the definition of transition relationship of the action variable
        '''
          
        action = "      next(action) := case\n "
        action += "                     grid[i][j] = 1 : no-action;\n"

        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[0])):
                if self.__grid[i][j] == 1 or (i, j) == self.__goal:
                    continue

                possible_action = self.possibile_action((i, j))
                if len(list(possible_action)) > 0:
                    action += "                     (i = {0}) & (j = {1}) : {2};\n".format(i, j, possible_action)

            
        action = action.replace('\'', "")        
        action += "                     TRUE : no-action;\n"
        action += "                     esac;\n\n"
        
        return action



    def possibile_action(self, state):
        '''
        Calculate the possible actions, i.e. the legal actions enabled in that state that NuSMV must check to establish the correct action.

        Parameters
        ----------
        state : tuple of int
            The state for which legal action is calculated.


        Returns
        -------
        possible_actions : set of strings
            The set of legal action for the input state.
        '''
        
        possible_actions  = set()
        N = len(self.__grid)
        M = len(self.__grid[0])
        
        if state[0] - 1 >= 0:
            if self.__grid[state[0]-1][state[1]] != 1:
                possible_actions.add("up")

        if state[0] + 1 < N and state[1] - 1 >= 0:
            if self.__grid[state[0]+1][state[1]-1] != 1:
                possible_actions.add("left-down")

        
        if state[0] - 1 >= 0 and state[1] - 1 >= 0:
            if self.__grid[state[0]-1][state[1]-1] != 1:
                possible_actions.add("left-up")

        if state[1] - 1 >= 0:
            if self.__grid[state[0]][state[1]-1] != 1:
                possible_actions.add("left")

        if state[0] - 1 >= 0 and state[1] + 1 < M:
            if self.__grid[state[0]-1][state[1]+1] != 1:
                possible_actions.add("right-up")

        
        if state[0] + 1 < N and state[1] + 1 < M:
            if self.__grid[state[0]+1][state[1]+1] != 1:
                possible_actions.add("right-down")

        
        if state[1] + 1 < M:
            if self.__grid[state[0]][state[1]+1] != 1:
                possible_actions.add("right")

        if state[0] + 1 < N:
            if self.__grid[state[0]+1][state[1]] != 1:
                possible_actions.add("down")

        return possible_actions
    

    
    def i_coordinate_next_relation(self):
        '''
        Generates the definition of the transition relationship for the i variable.

        Returns
        -------
        action : string
            String containing the definition of transition relationship of the i variable
        '''
        
        i_coord = "      next(i) := case\n "
        i_coord += "              ((next(action) = down) | (next(action) = right-down) | (next(action) = left-down)) & (i + 1 < N) : i + 1;\n"
        i_coord += "               ((next(action) = up) | (next(action) = right-up) | (next(action) = left-up)) & (i - 1 >= 0): i - 1;\n"
        i_coord += "               TRUE : i;\n"
        i_coord += "               esac;\n\n"
        
        return i_coord

    
    
    def j_coordinate_next_relation(self):
        '''
        Generates the definition of the transition relationship for the j variable.

        Returns
        -------
        action : string
            String containing the definition of transition relationship of the j variable
        '''
        
        j_coord = "      next(j) := case\n "
        j_coord += "              ((next(action) = right) | (next(action) = right-up) | (next(action) = right-down)) & (j + 1 < M): j + 1;\n"
        j_coord += "               ((next(action) = left) | (next(action) = left-up) | (next(action) = left-down)) & (j - 1 >= 0) : j - 1;\n"
        j_coord += "               TRUE : j;\n"
        j_coord += "               esac;\n\n"
        
        return j_coord


    
    def generate_ltl_specification(self):
        '''
        Sub-routine that generates the part of the model containing the LTL specification for verification.

        Returns
        -------
        model_specification : string
           String containing the LTL specification of the model.
        '''
        
        model_specification = "\n   LTLSPEC\n\n"
        model_specification += "      !(F ((i = {0}) & (j = {1})))\n".format(self.__goal[0], self.__goal[1])
        return model_specification

    

    def get_model(self):
        '''
        Returns the generated NuSMV model

        Returns
        -------
        model : string
           String containing the generated NuSMV model.
        '''
        return self.__model





