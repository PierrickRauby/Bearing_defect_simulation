import numpy as np

class Defect(object):
    """
    Documentation to do
    """
    def __init__(self, a_L:int,a_N:int,a_lambda:np.ndarray,a_delta:np.ndarray):
        """
        Documentation to do
        """
        self.m_L=a_L # The length of the defect
        self.m_N=a_N # The number of intervals in the defect
        self.m_lambda=a_lambda # Array of the width of the intervals
        self.m_delta=a_delta # Array of the depth of the intervals
        # Width of the interval that will enter in contact with the RE
        self.m_lambda_filtered=self.filter_interval(self)[0]
        # Depth of the interval that will enter in contact with the RE
        self.m_delta_filtered=self.filter_interval(self)[1]
        # X position of the interval that will enter in contact with the RE
        self.m_x_pos_filtered=self.filter_interval(self)[2] #

    def filter_interval(self):
        """
        Documentation to do
        """
        i=0
        m_lambda_filtered=np.empty(shape=(0,0))
        m_delta_filtered=np.empty(shape=(0,0))
        m_x_pos_filtered=np.empty(shape=(0,0))
        while (i<self.m_N-1):
            #find the next highest interval and go to it 
            i=np.argmin(self.m_delta[i+1:])
            m_lambda_filtered=np.append(self.m_lambda[i])
            m_delta_filtered=np.append(self.m_delta[i])
            m_x_pos_filtered=np.append(np.sum(self.m_lambda[0:i-1])
        return (m_lambda_filtered,m_delta_filtered,m_x_pos_filtered)


