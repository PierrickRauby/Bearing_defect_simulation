import numpy as np

class Defect(object):
    """
    Defect Object class
    """
    def __init__(self, a_L:float,a_N:int,a_lambda:np.ndarray,a_delta:np.ndarray):
        self.m_L=a_L # The length of the defect
        self.m_N=a_N # The number of intervals in the defect
        self.m_lambda=np.append(a_lambda,[0]) # Width of intervals
        self.m_delta=np.append(a_delta,[0]) # Depth of the intervals
        # Calculcate the intervals that will contact the rolling element
        filtered_intervals=self.filter_interval()
        # store their index for future use
        self.m_index_filtered=filtered_intervals[0]
        # Width of the interval that will enter in contact with the RE
        self.m_lambda_filtered=filtered_intervals[1]
        # Depth of the interval that will enter in contact with the RE
        self.m_delta_filtered=filtered_intervals[2]
        # X position of the interval that will enter in contact with the RE
        self.m_x_pos_filtered=filtered_intervals[3]

    def filter_interval(self):
        """
        Extract the intervals that will be in contact with the rolling element
        """
        i=0
        m_index_filtered=[]
        m_lambda_filtered=np.array([])
        m_delta_filtered=np.array([])
        m_x_pos_filtered=np.array([])
        for i in range(self.m_N+1):
            if np.argmin(self.m_delta[i:])==0:
                m_index_filtered.append(i)
                m_lambda_filtered=np.append(m_lambda_filtered,\
                        [self.m_lambda[i]])
                m_delta_filtered=np.append(m_delta_filtered,[self.m_delta[i]])
                m_x_pos_filtered=np.append(m_x_pos_filtered,\
                        [np.sum(self.m_lambda[0:i])])

        return (m_index_filtered,m_lambda_filtered,m_delta_filtered,m_x_pos_filtered)


