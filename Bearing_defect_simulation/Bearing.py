import sys 
sys.path.append('../')

from Bearing_defect_simulation.Bearing import RollingElement
from Bearing_defect_simulation.Defect import Defect
class Bearing(object):
    """
    Documentation to do 
    """
    def __init(self,a_n:int,a_dP:float,a_innerRace:bool,a_outerRace:bool,
            a_rpm:int,a_ballList:List[RollingElement],a_defect:Defect,
            a_theta:float):
        self.m_n=a_n # The number of rolling element
        self.m_dP=a_dP # The pitch diameter of the bearing
        self.m_innerRace=a_innerRace # True if working on the outer race
        self.m_outerRace=a_outerRace # True if working on the inner race
        self.m_rpm=a_rpm # Rpm of the bearing (rev/min)
        self.m_ballList=a_ballList # Array of the ball object
        self.m_defect=a_defect # The defect affecting the race
        self.m_theta=a_theta # The contact angle of the bearing 
