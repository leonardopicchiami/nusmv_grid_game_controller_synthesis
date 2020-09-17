####################################################################################################
#                                                                                                  #
# FileName    [controller_exception.py]                                                            #
#                                                                                                  #
# PackageName [exception]                                                                          #
#                                                                                                  #
# Synopsis    [This file contains the exception classes used in parsing the controller synthesis   #   
#              to handle incorrect cases.]                                                         #
#                                                                                                  #
# Author      [Leonardo Picchiami]                                                                 #
#                                                                                                  #
####################################################################################################




class ControllerException(Exception):
    '''
    Generic exception class for controller. Class that directly inherits Exception, 
    will never be raised acting as a superclass to the incorrect controller cases.
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(ControllerException, self).__init__(message)






class StateNotInSpaceControllerException(ControllerException):
    '''
    Exception class indicating that the input state is not in the state space. 
    So at least one of the two indices (or both) is not between 0 and its size.
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(StateNotInSpaceControllerException, self).__init__(message)



class ControllerNotSynthesizedControllerException(ControllerException):
    '''
    Exception class indicating that the controller has not yet been generated. 
    The K function cannot be used.
    '''
    
    def __init__(self, message):
        '''
        Parameters
        ----------
        message : string
            String message containing the explanation of the error that will be printed on the stderr.
        '''
        
        super(ControllerNotSynthesizedControllerException, self).__init__(message)

