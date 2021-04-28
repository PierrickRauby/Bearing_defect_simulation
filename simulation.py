import sys
import numpy as np
sys.path.append('../')
from Bearing_defect_simulation.DES.Simulation import Simulation
from Bearing_defect_simulation.Bearing.Bearing import Bearing
from Bearing_defect_simulation.Bearing.RollingElement import RollingElement
from Bearing_defect_simulation.DES.Acquisition import Acquisition

import argparse

def main(a_n:int=16,a_dP:float=71.501,a_race:str='outer',
            a_rpm:int=2000,a_dB:float=8.4074,a_theta:float=15.17,
            a_L:float=3.8,a_N:int=5,
            a_lambda:np.ndarray=[0.7,0.7,0.8,0.8,0.8],
            a_delta:np.ndarray=[0.5,0,0.5,0,0.7],
            a_duration:float=1,a_frequency:float=20000,a_noise:float=0.1):
    # Create the bearing
    if(a_lambda==None):
        a_lambda=np.array([0.7,0.7,0.8,0.8,0.8])
    if(a_delta==None):
        a_delta=np.array([0.5,0,0.5,0,0.7])
    my_bearing=Bearing(a_n=a_n,a_dP=a_dP,a_race=a_race,
            a_rpm=a_rpm,a_dB=a_dB,a_theta=a_theta,
            a_L=a_L,a_N=a_N,a_lambda=a_lambda,a_delta=a_delta)
    # Create an Acquisition
    my_acquisition=Acquisition(a_duration=a_duration,a_frequency=a_frequency,
            a_noise=a_noise)
    #Create a simulation
    my_simulation=Simulation(my_bearing,my_acquisition)
    #start a simulation 
    my_simulation.start()
    my_simulation.get_results(format='show')



def invoke_parser():
    """
    Command line 
    Positional arguments for desired paths.
    Optional arguments for all the options. 
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n", nargs='?', type=int,default='16',
        help="The Number of rolling element in the bearing."
    )
    parser.add_argument(
        "--dP", nargs='?', type=float,default='71.501',
        help="The Pitch Diameter of the bearing (mm)."
    )
    parser.add_argument(
        "--race", nargs='?', type=str,default='outer',
        help="The race affected by the defect, can be 'inner' or 'outer'."
    )
    parser.add_argument(
        "--rpm", nargs='?', type=int,default='2000',
        help="The rotational speed of the bearing (rpm)"
    )
    parser.add_argument(
        "--dB", nargs='?', type=float,default='8.4074',
        help="The Rolling Element Diameter (mm)."
    )
    parser.add_argument(
        "--theta", nargs='?', type=float,default='15.17',
        help="The contact angle of the bearing (deg)."
    )
    parser.add_argument(
        "--L", nargs='?', type=float,default='3.8',
        help="The length of the defect (mm)."
    )
    parser.add_argument(
        "--N", nargs='?', type=int,default='5',
        help="The number of interval of the defect."
    )
    parser.add_argument(
        "--a_lambda", nargs='+',
        help="The different lengths of the intervals representing the defect."
    )
    parser.add_argument(
        "--a_delta", nargs='+',
        help="The different depths of the intervals representing the defect."
    )
    parser.add_argument(
        "--duration", nargs='?', type=float,default='1',
        help="The duration of the simulation (s)."
    )
    parser.add_argument(
        "--frequency", nargs='?', type=float,default='20000',
        help="The time resolution of the simulation (Hz)."
    )
    parser.add_argument(
        "--noise", nargs='?', type=float,default='0.1',
        help="The ratio of noise added in the simulation (between 0.0 and 0.9)."
    )

    return parser

if __name__ == '__main__':
    parser = invoke_parser()
    FLAGS = parser.parse_args()  # parses the command line argument
    main(a_n=FLAGS.n,a_dP=FLAGS.dP,a_race=FLAGS.race,
            a_rpm=FLAGS.rpm,a_dB=FLAGS.dB,a_theta=FLAGS.theta,
            a_L=FLAGS.L,a_N=FLAGS.N,
            a_lambda=np.array(FLAGS.a_lambda),
            a_delta=np.array(FLAGS.a_delta),
            a_duration=FLAGS.duration,
            a_frequency=FLAGS.frequency,
            a_noise=FLAGS.noise,
            )
