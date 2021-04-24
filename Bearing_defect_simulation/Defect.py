import numpy as np

class Defect(object):
    """
    Documentation to do
    """
    def __init__(self, a_L:int,a_N:int,a_lambda:np.ndarray,a_delta:np.ndarray):
        self.m_L=a_L # The length of the defect
        self.m_N=a_N # The number of intervals in the defect
        self.m_lambda=a_lambda # Array of the width of the intervals
        self.m_delta=a_delta # Array of the depth of the intervals

