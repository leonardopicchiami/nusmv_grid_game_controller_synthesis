#############################################################################################################################################
#                                                                                                                                           #
# FileName      [pycode_generator.py]                                                                                                       #
#                                                                                                                                           # 
# PackageName   [code_generator]                                                                                                            #
#                                                                                                                                           # 
# Synopsis      [This file contains the class that generates the Python code of the K function in the generation of the controller          #
#                and the Legal function, enabling all the legal actions of each cell (if they exist for that cell).]                        #
#                                                                                                                                           #
# Author        [Leonardo Picchiami]                                                                                                        #
#                                                                                                                                           #
#############################################################################################################################################



class PyCodeGenerator(object):
    '''
    Class that generates the Python code of the K function in the generation of the controller 
    and the Legal function, enabling all the legal actions of each cell (if they exist for that cell).


    Attributes
    ----------
    code_file_path : string
        Path of the output file.

    code_file_name : string
        Name of the output file.
    '''

    
    def __init__(self, code_file_path, code_file_name):
        '''
        Class constructor.

        Parameters
        ----------
        code_file_path : string
            Path of the output file.

        code_file_name : string
            Name of the output file.

        file_descriptor : TextIoWrapper (File), default None
            Object that manages the file when writing functions.
        '''
        
        self.__code_file_path = code_file_path
        self.__code_file_name = code_file_name
        self.__file_descriptor = None

        
    def start(self):
        '''
        Create the full path of the output python file eapre the descriptor file by creating a new file for writing.
        '''
        
        if self.__code_file_path[-1]  != '/':
           self.__code_file_path += '/'

        complete_path = self.__code_file_path + self.__code_file_name
        self.__file_descriptor = open(complete_path, "w")

        

    def write_K_function(self, states_actions_set, N, M):
        '''
        Writes the K function to the output file. 
        Use the correct state-action pairs to define which actions, of the states belonging to the set of controllable states, are enabled and therefore return True.

        Parameters
        ----------
        states_actions_set : set of tuples
            Set of state-action pairs where each action is a correct action for that state.
        '''
        
        self.__file_descriptor.write("def K(state, action):\n\n")
        self.write_state_control(N, M)
        self.write_action_control()

        for s_a in states_actions_set:
            self.__file_descriptor.write("    if state == {0} and action.lower() == \"{1}\":\n".format(s_a[0], s_a[1]))
            self.__file_descriptor.write("        return True\n\n")

        self.__file_descriptor.write("    return False\n\n\n\n")
            

        
    def write_Legal_function(self, grid, goal):
        '''
        Writes the Legal function to the output file. 
        Check the cell lawsuits, regardless of whether we have at least one path leading to the goal or not.

        Parameters
        ---------
        grid : matrix of int
            The game grid

        goal : tuple of int
            The goal cell.
        '''
        
        self.__file_descriptor.write("def Legal(state, action):\n\n")
        self.write_state_control(len(grid), len(grid[0]))
        self.write_action_control()

        
        N = len(grid)
        M = len(grid[0])
    
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    continue

                #if (i, j) == goal:
                #    continue
                
                if (i - 1 >= 0) and (j - 1 >= 0):
                    if grid[i-1][j-1] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"left-up\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if i - 1 >= 0:
                    if grid[i-1][j] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"up\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if (i - 1 >= 0) and (j + 1 < M):
                    if grid[i-1][j+1] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"right-up\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if j + 1 < M:
                    if grid[i][j+1] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"right\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if (i + 1 < N) and (j + 1 < M):
                    if grid[i+1][j+1] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"right-down\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if i + 1 < N:
                    if grid[i+1][j] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"down\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if (i + 1 < N) and (j -1 >= 0):
                    if grid[i+1][j-1] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"left-down\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")

                if j - 1 >= 0:
                    if grid[i][j-1] != 1:
                        self.__file_descriptor.write("    if state == {0} and action.lower() == \"left\":\n".format((i, j)))
                        self.__file_descriptor.write("        return True\n\n")
                        
        self.__file_descriptor.write("    return False\n\n\n\n".format((i, j)))
                                                    


    def write_state_control(self, N, M):
        '''
        Writes to the output file the control necessary to establish whether the input state is a state present in the grid.

        Parameters
        ----------
        N : int
            Number of grid rows.

        M : int
           Number of grid columns.
        '''
        
        self.__file_descriptor.write("    if (state[0] < 0 or state[0] >= {0}) or (state[1] < 0 or state[1] >= {1}):\n".format(N, M))
        self.__file_descriptor.write("        raise Exception(\"The input state is not among the grid states.\")\n\n")


        
    def write_action_control(self):
        '''
        Writes to the output file the control necessary to establish whether the input action is one of the actions that can be performed in the grid.
        '''
        
        self.__file_descriptor.write("    if action.lower() not in [\"up\", \"left-up\", \"right-up\", \"right\", \"right-down\", \"down\", \"left-down\", \"left\"]:\n")
        self.__file_descriptor.write("        raise Exception(\"The input action is not among the actions that can be performed.\")\n\n")

        
        
    def close_file(self):
        '''
        Closes the previously opened file descriptor of the output file.
        '''
        
        self.__file_descriptor.close()

     
        
        
    
