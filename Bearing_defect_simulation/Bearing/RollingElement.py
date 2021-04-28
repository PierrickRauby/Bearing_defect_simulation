class RollingElement(object):
    """
    Rolling element class
    """
    def __init__(self,a_dB:float,a_duration:float):
        self.m_dB=a_dB # The diameter of the ball (mm)
        self.m_duration=a_duration # The duration spent by the ball in
                                   # the defect
        self.m_x_pos_in_defect=0.0 # position of the ball in the defect region
        self.m_index_interval_touched=[] #index touched by the ball
    def advance(self,dx):
        self.m_x_pos_in_defect+=dx
