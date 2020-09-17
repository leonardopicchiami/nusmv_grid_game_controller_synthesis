#############################################################################################################################
#                                                                                                                           #
# FileName    [model_checker_parsing.py]                                                                                    # 
#                                                                                                                           #   
# PackageName [parsing]                                                                                                     # 
#                                                                                                                           #
# Synopsis    [This file contains the class that analyzes the counterexample, if it exists, that returns NuSMV              #
#              so that we can extrapolate all the crossed cells, elaborate carefully for each cell that leads to the goal   #
#              or simply check if there is a counterexample (if there is at least one path from the start to the goal).]    #                                              #
#                                                                                                                           #
# Author      [Leonardo Picchiami]                                                                                          #
#                                                                                                                           #
#############################################################################################################################




class ModelCheckerParsing(object):
    '''
    Class that analyzes the counterexample, if it exists, that returns NuSMV so that we can extrapolate all the crossed cells, 
    elaborate carefully for each cell that leads to the goal or simply check if there is a counterexample (if there is at least one path from the start to the goal).

    Attributes
    ----------
    grid : matrix of int
       matrix that represents the game grid

    result : string
       String representing the output of the model checker.
    '''

    
    def __init__(self, result):
        '''
        Parameters
        ----------
        result : string
           Model checker output
        '''
        
        self.__state_action = []
        self.__result = result.decode()

        
         
    def exists_path_init_to_goal(self, goal):
        '''
        Check if there is a counterexample or not.

        Parameters
        ----------
        goal : tuple of int
           Goal cell of the grid needed for the ctl specification.

        Returns
        -------
        boolean
           True if there is a counterexample, false otherwise.
        '''
        
        if "-- specification !( F (i = {0} & j = {1}))  is false".format(goal[0], goal[1]) in self.__result:
            return True

        return False


    
    def parse_state_action_conterexample(self):
        '''
        Analyzes all the cells of the grid indicated by the counterexample, extrapolating for each cell the action by which that cell was reached. 
        Except for the initial state, NuSMV indicates only the values of the coordinates, i, j and / or the action that leads to that cell.
        '''
        
        result_list = self.__result.split('\n')

        tmp_i = 0
        tmp_j = 0
        tmp_action = ""
        new_state_action = False

        for line in result_list:
            if "-- Loop starts here" in line:
                if new_state_action:
                    self.__state_action.append(((tmp_i, tmp_j), tmp_action))
                    new_state_action = False
                return

        
            if "action = " in line:
                tmp_action = line[13:]
                new_state_action = True

            if "i = " in line and "-- specification" not in line:
                tmp_i = int(line[8:])
                new_state_action = True

            
            if "j = " in line and "-- specification"  not in line:
                tmp_j = int(line[8:])
                new_state_action = True

            
            if "-> State" in line or result_list.index(line) == len(result_list) - 1:
                if new_state_action:
                    self.__state_action.append(((tmp_i, tmp_j), tmp_action))
                    new_state_action = False
                continue

            

                

    def get_state_action(self):
        '''
        Returns the set of pairs: state - correct action for which that state was reached.

        Returns
        -------
        state_action : list of tuples
            List of pairs: state - correct action for which that state was reached.
        '''
        
        return self.__state_action



    def get_correct_state_action(self):
        '''
        Returns the pair that represents the state-action pair where the state represents the state being processed and the action is the correct action returned by NuSMV.

        Returns
        -------
        tuple : tuple of state-action
            Pair that represents the state-action where the state represents the state being processed and the action is the correct action returned by NuSMV.
        '''
        if len(self.__state_action) > 1:
            return ((self.__state_action[0][0], self.__state_action[1][1]))

        return None

    
    def get_postprocessed_state_action(self):
        '''
        Returns a list of state-action pairs, an correct action from that state, after a post-processing phase.

        Returns
        -------
        post_state_action : list of tuples
          list of state-action pairs after the post-processing phase.
        '''
        
        post_state_action = []
        for i in range(len(self.__state_action) - 1):
            post_state_action.append((self.__state_action[i][0], self.__state_action[i + 1][1]))

        return post_state_action


    
    def get_crossed_states(self):
        '''
        Returns the list of cells that have been crossed (therefore the list of cells where there is a path leading to the goal).

        Returns
        -------
        visited_states : list of tuples of int
           List of coordinates of the cells that were visited during the verification.
        '''
        
        crossed_states = [s_a[0] for s_a in self.__state_action]
        return crossed_states
