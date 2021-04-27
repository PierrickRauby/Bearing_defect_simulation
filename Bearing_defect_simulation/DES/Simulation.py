import sys
import math
import numpy as np
import time
from threading import Thread

sys.path.append('../')
from Bearing_defect_simulation.Bearing.Bearing import Bearing
from Bearing_defect_simulation.Bearing.RollingElement import RollingElement
from Bearing_defect_simulation.DES.Acquisition import Acquisition

# TODO: not sure if I use all of them
# from Bearing_defect_simulation.DES.engine import simulate
# import Bearing_defect_simulation.DES.event_management
# import Bearing_defect_simulation.DES.simu_time

class Simulation(object):
    """
    Documentation TODO
    """
    def __init__(self,bearing:Bearing,acquisition:Acquisition):
        #Calculate the number of ball to pass on the defect
        if bearing.m_outerRace:
            self.m_n_ball_to_pass=round(acquisition.m_duration*\
                    bearing.get_BPFO_freq())
        else:
            self.m_n_ball_to_pass=round(acquisition.m_duration*\
                    bearing.get_BPFI_freq())
        # Create a list of ball to pass in the defect,
        # Note: the ball are new instance of RollingElement and are not related 
        #       to the ones in the bearing 
        self.m_ballList=[RollingElement(bearing.m_dB,bearing.m_duration) \
                for i in range(self.m_n_ball_to_pass)]
        self.m_bearing=bearing
        self.m_acquisition=acquisition

        # Create a thread per ball, but don't start it
        # TODO: check speed with thread and processes, be carefull needs a lot 
        # of modification for multiprocessing 

        self.m_threads=[]
        for i,ball in  enumerate(self.m_ballList):
            #Creat the treads
            self.m_threads.append(Thread(target=self.run_ball_throught_defect,\
                    args=(i,ball)))
        self.get_info()

    def run_ball_throught_defect(self,i:int,ball:RollingElement):
        # time in the simulation were the ball simulated by the current thread 
        # enters the defect region
        time_enter_defect=i*self.m_bearing.m_duration_between_ball
        time_exit_defect=time_enter_defect+ball.m_duration
        # run for all dt where the ball is in the defect region
        #advange along x during dt
        dx=self.m_acquisition.m_dt/ball.m_duration*self.m_bearing.m_defect.m_L
        dt=time_enter_defect
        while(dt<time_exit_defect):
            dt+=self.m_acquisition.m_dt
            ball.advance(dx)
            interval_underball=self.find_interval_under_ball(ball,i)
            if(interval_underball):
                if i==0:
                    print("contact interval: "+str(interval_underball))
                # contact I store the results
            else:
                # no contact I advance by dt
                continue
        return 0

    def get_amplitude(self,ball:RollingElement,i:int):




        return 0


    def find_interval_under_ball(self,ball:RollingElement,j):
        # finds the interval under the ball and return the interval if it makes
        # contact
        # if j==0:
            # print("interval at: "+str(self.m_bearing.m_defect.m_x_pos_filtered))
        for k in range(len(self.m_bearing.m_defect.m_x_pos_filtered)):
            gogo=0
            if j==0 and gogo==0:
                gogo=1
                print("First invocation")
            ball_position=ball.m_x_pos_in_defect
            begin_interval=self.m_bearing.m_defect.m_x_pos_filtered[k]
            end_interval=self.m_bearing.m_defect.m_x_pos_filtered[k]+\
                    self.m_bearing.m_defect.m_lambda_filtered[k]

            if(begin_interval<ball_position and ball_position<end_interval):
                if k not in ball.m_index_interval_touched:
                    ball.m_index_interval_touched.append(k)
                    if j==0:
                        print("ball_position "+str(ball_position))
                        print("begin_interval "+str(begin_interval))
                        print("end_interval "+str(end_interval))
                        print("-----> contact:"+str(self.m_bearing.m_defect.m_index_filtered[k]))
                        print("#######")
                    return self.m_bearing.m_defect.m_index_filtered[k]
                else: continue
            if(begin_interval==self.m_bearing.m_defect.m_L 
                    and begin_interval<ball_position):
                if j==0:
                    print("last interval detected")
                    print("ball_position "+str(ball_position))
                    print("begin_interval "+str(begin_interval))
                    print("end_interval "+str(end_interval))
                    print("-----> contact:"+str(self.m_bearing.m_defect.m_index_filtered[k]))
                    print("#######")
                return self.m_bearing.m_defect.m_index_filtered[k]
        return 0

#
#
#            #advance the distance
#            # distance+=self.m_bearing.m_defect.m_x_pos_filtered[i]
#
#            if j==0:
#                print("ball at: "+str(ball.m_x_pos_in_defect))
#                print("distance at: "+str(distance))
#            # check if the ball is this interval
#            if distance < ball.m_x_pos_in_defect:
#
#                # if j==0:
#                    # print(str(j)+"next")
#                continue
#            else:
#                # print("interval i "+str(i))
#                return i
#            distance=self.m_bearing.m_defect.m_x_pos_filtered[i]
#

#                # if j==0:
#                    # print(str(j)+"bellow ball")
#                if i in self.m_bearing.m_defect.m_index_filtered:
#                    if j==0:
#                        print("contact")
#                    return i
#                else:
#                    return 0


    def start(self):
        time_start=time.time()
        print("fonction to implement")
        for t in self.m_threads:
            t.start()
        for t in self.m_threads:
            t.join()
        print("simulation completed in "+str(time.time()-time_start)+"s.")

    def get_results(self,format:str):
        print("TODO: Implement this function")
        if format=='as_array':
            print('output formated as array')
        elif format=='as_file':
            print('output formated as file')
        elif format=='as_graph':
            print('output formated as graph')
        else:
            print("Err: format unknown")


    def get_info(self):
        self.m_bearing.get_info()
        self.m_acquisition.get_info()
        print("################# SIMULATION PARAM  ############## ")
        print("#")
        print("#  Simulation created")
        print("#  Number of ball to pass on the defect:"+\
                str(self.m_n_ball_to_pass))
        print("#")
        print("################################################### ")
        if(input("Do you want to start the simulation?(y/n)")=='y'):
                self.start()
        else:
            print("ok I won't do anything")





