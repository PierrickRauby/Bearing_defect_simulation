import sys
import math
import numpy as np

sys.path.append('../')

from Bearing_defect_simulation.Bearing.RollingElement import RollingElement
from Bearing_defect_simulation.Bearing.Defect import Defect

class Bearing(object):
    """
    Documentation TODO
    """
    def __init__(self,a_n:int=16,a_dP:float=71.501,a_race:str='outer',
            a_rpm:int=2000,a_dB:float=8.4074,a_theta:float=15.17,
            a_L:float=3.8,a_N:int=5,
            a_lambda:np.ndarray=[0.7,0.7,0.8,0.8,0.8],
            a_delta:np.ndarray=[0.5,0,0.5,0,0.7]):

    # def __init__(self,a_n:int=16,a_dP:float=71.501,a_race:str='outer',
            # a_rpm:int=2000,a_dB:float=8.4074,a_theta:float=15.17,
            # a_L:int=0.1,a_N:int=1,
            # a_lambda:np.ndarray=[0.1],a_delta:np.ndarray=[0.1]):
        self.m_n=a_n # The number of rolling element
        self.m_dP=a_dP # The pitch diameter of the bearing
        self.m_dB=a_dB # The diameter of the rolling element 
        if a_race=='inner':
            self.m_innerRace=True # True if working on the outer race
        elif a_race=='outer':
            self.m_outerRace=True # True if working on the inner race
        else: # TODO: handle error in a better way
            print("error ! Race should be either 'inner' or 'outer'")
            return 1
        self.m_rpm=a_rpm/60 # Rpm of the bearing (rev/min)->(rad/s)
        # The duration spent by a ball on the bearing defect (from eq it does
        # not depends on the race affected
        self.m_duration=2*a_L*a_dP/(self.m_rpm*math.pi\
                *(a_dP**2-(a_dB*math.cos(a_theta))**2))
        #Create the rolling elements, note that they are not used at any point
        #   I have only created that to reflect the reality of a Rolling Element
        #   bearing, and in case we don't want all the ball to be the same
        #   for example we can image a ball to be smaller than the others
        self.m_ballList=[RollingElement(a_dB,self.m_duration) \
                for i in range(self.m_n)]
        for i in range(self.m_n):
            self.m_ballList.append(RollingElement(a_dB,self.m_duration))

        self.m_defect=Defect(a_L,a_N,a_lambda,a_delta)
        self.m_theta=a_theta*math.pi/180 # The contact
        self.m_duration_between_ball=1/self.get_BPFO_freq()
                #angle of the bearing (deg)->(rad)
        #TODO: keep or remove the next line 
        # self.get_info()

    def get_BPFO_freq(self):
        # See proposal page 3 for the derivation of the BPFO defect frequencies
        defect_frequency=self.m_n/2*self.m_rpm*\
                (1-self.m_dB/self.m_dP*math.cos(self.m_theta))
        return defect_frequency

    def get_BPFI_freq(self):
        # See proposal page 3 for the derivation of the BPFI defect frequencies
        defect_frequency=self.m_n/2*self.m_rpm*\
                (1+self.m_dB/self.m_dP*math.cos(self.m_theta))
        return defect_frequency

    def get_info(self):
        print("################# BEARING CREATED ################# ")
        print("#                                                  ")
        print("#  Number Rolling Elements:"+str(self.m_n))
        print("#  RPM: "+str(round(100*self.m_rpm)/100)+"Hz")
        print("#  Pitch Diameter: "+str(self.m_dP)+"mm")
        print("#  Rolling Element Diameter: "+str(self.m_dB)+"mm")
        print("#  BPFO Frequency: "+str(round(100*self.get_BPFO_freq())/100)+"Hz")
        print("#  BPFI Frequency: "+str(round(100*self.get_BPFI_freq())/100)+"Hz")
        print("#  Duration spent by a Rolling Element in the defect: "\
                +str(round(1000*self.m_duration)/1000)+"s")
        print("#  Duration between the passage of 2 Rolling element: "\
                +str(round(1000*1/self.get_BPFO_freq())/1000)+"s")
        print("#                                                  ")
        return 0
