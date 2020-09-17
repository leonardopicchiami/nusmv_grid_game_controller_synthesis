#################################################################################################
#                                                                                               #
# FileName    [input_exeception.py]                                                             # 
#                                                                                               #
# PackageName [exception]                                                                       #
#                                                                                               #
# Synopsis    [This file contains the exception classes used in parsing the input file          #
#              to handle incorrect specification cases in the file.]                            #
#                                                                                               #
# Author      [Leonardo Picchiami]                                                              #
#                                                                                               #
#################################################################################################






class InputException(Exception):
    '''
    Generic exception class for input file. Class that directly inherits Exception, 
    will never be raised acting as a superclass to the input specification contrains.
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputException, self).__init__(message)



class InputNoNumberOfLinesException(InputException):
    '''
    Exception class indicating an error about specifying the size of the rows.
    Either the size is less than 2 or the specification is absent. 
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputNoNumberOfLinesException, self).__init__(message)



class InputNoNumberOfColumnsException(InputException):
    '''
    Exception class indicating an error about specifying the size of the columns.
    Either the size is less than 2 or the specification is absent.
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputNoNumberOfColumnsException, self).__init__(message)



class InputNoInitException(InputException):
    '''
    Exception class indicating an error about specifying the init coordinates.
    The coordinates of the init cell were not specified. 
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputNoInitException, self).__init__(message)




class InputNoGoalException(InputException):
    '''
    Exception class indicating an error about specifying the goal coordinates.
    The coordinates of the goal cell were not specified. 
    '''
     
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputNoGoalException, self).__init__(message)




class InputNoGridException(InputException):
    '''
    Exception class indicating an error about specifying the game grid.
    The game grid were not specified. 
    '''

    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputNoGridException, self).__init__(message)



class InputGridDimensionException(InputException):
    '''
    Exception class indicating an error about specifying the init coordinates.
    The coordinates of the init cell were not specified. 
    '''

    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputGridDimensionException, self).__init__(message)



class InputInitOutOfBoundException(InputException):
    '''
    Exception class indicating an error about specifying the init coordinates.
    The coordinates of the init cell are outside the grid. 
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputInitOutOfBoundException, self).__init__(message)



class InputGoalOutOfBoundException(InputException):
    '''
    Exception class indicating an error about specifying the goal coordinates.
    The coordinates of the goal cell are outside the grid. 
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputGoalOutOfBoundException, self).__init__(message)



class  InputInitOrGoalObstaclesException(InputException):
    '''
    Exception class indicating an error about specifying the grid.
    The grid has an obstacle in the init cell or in the goal cell.
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(InputInitOrGoalObstaclesException, self).__init__(message)


