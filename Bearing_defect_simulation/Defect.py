import numpy as np

class Defect(object):
    """
    Documentation to do
    """
    def __init__(self, a_L:int,a_N:int,a_lambda:np.ndarray,a_delta:np.ndarray):
        self.m_L=a_L # The length of the defect
        self.m_N=a_N # The number of intervals in the defect
        self.intervals=
        self.m_lambda=a_lambda # Array of the width of the intervals
        self.m_delta=a_delta # Array of the depth of the intervals
# TODO: on creation update the defect with the intervals of contact 
#   (contact if min depth on the following intervals )
        self.m_lambda_filtered=self.filter_interval(
        self.m_lambda_filtered=


    def filter_interval
