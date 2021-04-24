import sys
import math

sys.path.append('../')

from Bearing_defect_simulation.Bearing import RollingElement
from Bearing_defect_simulation.Defect import Defect
class Bearing(object):
    """
    Documentation to do 
    """
    def __init__(self,a_n:int,a_dP:float,a_innerRace:bool,a_outerRace:bool,
            a_rpm:int,a_dB:float, a_theta:float,a_L:int,a_N:int,
            a_lambda:np.ndarray,a_delta:np.ndarray):
        self.m_n=a_n # The number of rolling element
        self.m_dP=a_dP # The pitch diameter of the bearing
        if a_race=='inner':
            self.m_innerRace=a_innerRace # True if working on the outer race
        elif a_race=='outer':
            self.m_outerRace=a_outerRace # True if working on the inner race
        else: # TODO: handle error in a better way
            print("error ! Race should be either 'inner' or 'outer'")
            return 1
        self.m_rpm=a_rpm # Rpm of the bearing (rev/min)
        # The duration spent by a ball on the bearing defect (from eq it does
        # not depends on the race affected
        duration=2*a_L*a_dP/(math.pi*(a_dP**2-(a_dB*math.cos(a_theta))**2))
        #Create the rolling elements 
        self.m_ballList=[RollingElement(a_dB,duration) for i in range(self.m_n)]
        for i in range(self.m_n):
            self.m_ballList.append(RollingElement(a_dB,duration))

        self.m_defect=Defect(a_L,a_N,a_Lambda,a_delta)
        self.m_theta=a_theta # The contact angle of the bearing 

    def get_BPFO_freq(self):
        # See proposal page 3 for the derivation of the BPFO defect frequencies
        defect_frequency=self.m_n/2*self.m_rpm*\
                (1-m_ballList[0].m_dB/self.m_dP*math.cos(self.m_theta))
        return 

    def get_BPFI_freq(self):
        # See proposal page 3 for the derivation of the BPFI defect frequencies
        defect_frequency=self.m_n/2*self.m_rpm*\
                (1+m_ballList[0].m_dB/self.m_dP*math.cos(self.m_theta))
        return 
