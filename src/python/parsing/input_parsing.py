################################################################################################################################################
#                                                                                                                                              #
# FileName    [input_parsing.py]                                                                                                               #
#                                                                                                                                              #
# PackageName [parsing]                                                                                                                        #
#                                                                                                                                              #
# Synopsis    [This file contains the class for parsing the input file and obtaining initial cell, goal cell, grid,                            #
#              and relative grid size. You can either parser the grid from the file or generate it randomly depending on what is required.]    #
#                                                                                                                                              #
# Author      [Leonardo Picchiami]                                                                                                             #
#                                                                                                                                              #
################################################################################################################################################


import random

import exception.input_exception as excpt


class InputParser(object):
    '''
    Class for parsing the input file and obtaining initial cell, goal cell, grid, and relative grid size. 
    You can either parser the grid from the file or generate it randomly depending on what is required.
    

    Attributes
    ---------
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

    
    
    def __init__(self):
        '''
        Class constructor.
        '''
        
        self.__n = 0
        self.__m = 0
        self.__grid = []
        self.__init = None
        self.__goal = None    
        

        
    def file_nogrid_parser(self, path, exist_flag):
        '''
        Parses the input file excluding the grid. 
        In this case it is generated randomly by imposing that both the init and the goal do not have an obstacle in the cell.

        Parameters
        ----------
        path : string
           Input file path.

        exits_flag : boolean
           Flag indicating whether the system should only check if there is a path from the start to the goal or not. 
           It is used to consider the init or not.
        '''
        
        with open(path, "r") as f:
            for line in f:
                if "goal" in line.lower():
                    self.goal_parser(line)
                if "init" in line.lower():
                    self.init_parser(line) 
                if "n" in line.lower():
                    self.lines_dimension_parser(line)
                if "m" in line.lower():
                    self.columns_dimension_parser(line)

        self.correctness_input_file(exist_flag)
        self.grid_random_generation(exist_flag)
        
                    
                    
    def file_grid_parser(self, path, exist_flag):
        '''
        Parses the input file (including the grid). 
        In this case the grid must be specified on the input file.

        Parameters
        ----------
        path : string
           Input file path.

        exits_flag : boolean
           Flag indicating whether the system should only check if there is a path from the start to the goal or not. 
           It is used to consider the init or not.
        '''

        is_grid = False
        with open(path, "r") as f:
            for line in f:
                if "goal" in line.lower():
                    self.goal_parser(line)
                elif "init" in line.lower():
                    self.init_parser(line)
                elif "n" in line.lower():
                    self.lines_dimension_parser(line)
                elif "m" in line.lower():
                    self.columns_dimension_parser(line)
                elif "grid" in line.lower():
                    is_grid = True

                elif is_grid:
                    is_grid = self.grid_parser(line)


        #Checking of input specification correctness
        self.correctness_input_file(exist_flag)
        
        if len(self.__grid) == 0:
            raise excpt.InputNoGridException("The input file no contains the game grid specification.")

        elif len(self.__grid) != self.__n or len(self.__grid[0]) != self.__m:
            raise excpt.InputGridDimensionException("The specified grid size is incorrect.")
            
        elif exist_flag:
            if self.__grid[self.__init[0]][self.__init[1]] == 1 or self.__grid[self.__goal[0]][self.__goal[1]] == 1:
                raise excpt.InputInitOrGoalObstaclesException("The coordinates of the goal or those of the init have an obstacle on the grid.")
        
        

    def goal_parser(self, file_line):
        '''
        Parses the goal cell input specification line (on input file).

        Parameters
        ----------
        file_line : string
           Line of the file that contains the coordinates of the goal cell.
        '''
        
        values = file_line.split()
        self.__goal = (int(values[1][1:-1]), int(values[2][:-1]))


        
    def init_parser(self, file_line):
        '''
        Parses the init cell input specification line (on input file).

        Parameters
        ----------
        file_line : string
           Line of the file that contains the coordinates of the init cell.
        '''
        
        values = file_line.split()
        self.__init = (int(values[1][1:-1]), int(values[2][:-1]))


        
    def grid_parser(self, file_line):
        '''
        Parses the grid input specification (from the input file).

        Parameters
        ----------
        file_line : string
           Line of the file that contains the first line of the input grid.
        '''
                
        elems = file_line.split()
        grid_row = []
        
        for i in elems:
            if i != "":
                grid_row.append(int(i))

        if len(grid_row) > 0:
            self.__grid.append(grid_row)
            return True

        return False

    

    def grid_random_generation(self, exist_flag):
        '''
        Randomly generates the grid. 
        It is also required that the init and goal cells have no obstacles.
        '''
        
        for i in range(self.__n):
            grid_row = []
            for j in range(self.__m):
                if exist_flag and (i == self.__init[0] and j == self.__init[1]):
                    grid_row.append(0)
                
                elif (i == self.__goal[0]) and (j == self.__goal[1]):
                    grid_row.append(0)

                else:
                    rand = random.randint(0, 1)
                    grid_row.append(rand)
                    
            self.__grid.append(grid_row)  
        

            
    def lines_dimension_parser(self, file_line):
        '''
        Parses the input specification of size of rows (from the input file).

        Parameters
        ----------
        file_line : string
           Line of the file that contains the specification of the numbers of rows.
        '''

        values = file_line.split()
        self.__n = int(values[1])


        
    def columns_dimension_parser(self, file_line):
        '''
        Parses the input specification of size of columns (from the input file).

        Parameters
        ----------
        file_line : string
           Line of the file that contains the first line of the input grid.
        '''

        values = file_line.split()
        self.__m = int(values[1])

        

    def correctness_input_file(self, exist_flag):
        '''
        Checks the correctness of the input specifications. 
        If there is a mistake, throw the appropriate exception.
        '''
        
        if self.__init == None and exist_flag:
            raise excpt.InputNoInitException("The input file no contains the init cell specification.")
            
        if self.__goal == None:
            raise excpt.InputNoGoalException("The input file no contains the goal cell specification.")

        if self.__n < 2:
            raise excpt.InputNoNumberOfLinesException("The input file no contains the the number of lines N specification or the value is less than 2.")

        if self.__m < 2:
            raise excpt.InputNoNumberOfColumnsException("The input file no contains the the number of columns M specification or the value is less than 2.")

        if self.__goal != None:
            if self.__goal[0] < 0 or self.__goal[0] >= self.__n:
                raise excpt.InputGoalOutOfBoundException("The coordinates of the goal cell are not included in the grid size.")

            if self.__goal[1] < 0 or self.__goal[1] >= self.__m:
                raise excpt.InputGoalOutOfBoundException("The coordinates of the goal cell are not included in the grid size.")

        if self.__init != None and exist_flag:
            if self.__init[0] < 0 or self.__init[0] >= self.__n:
                raise excpt.InputInitOutOfBoundException("The coordinates of the init cell are not included in the grid size.")

            if self.__init[1] < 0 or self.__init[1] >= self.__m:
                raise excpt.InputInitOutOfBoundException("The coordinates of the init cell are not included in the grid size.")


            
    def get_goal(self):
        '''
        Returns the goal cell of the grid.

        Returns
        -------
        goal : tuple of int
           Coordinates of the goal cell.
        '''
        
        return self.__goal


    
    def get_init(self):
        '''
        Returns the init cell of the grid.

        Returns
        -------
        init : tuple of int
           Coordinates of the init cell.
        '''
        return self.__init


    
    def get_grid(self):
        '''
        Returns the game grid.

        Returns
        -------
        grid : matrix of int
           NxM matrix of representing grid of the game.
        '''
        
        return self.__grid


    
    def get_n(self):
        '''
        Returns the number of grid rows.

        Returns
        -------
        n : int
           Number of grid rows.
        '''
        
        return self.__n


    
    def get_m(self):
        '''
        Returns the number of grid columns

        Returns
        -------
        m : int
           Number of grid columns.
        '''
        
        return self.__m

