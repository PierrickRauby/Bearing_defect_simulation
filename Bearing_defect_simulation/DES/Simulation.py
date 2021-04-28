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
        # Proportionality constant
        self.m_gamma=10

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
                amplitude=self.get_amplitude(ball,interval_underball)
                position_in_array=self.get_position_pulse_in_waveform\
                        (time_enter_defect,dt)
                self.m_acquisition.m_waveform[position_in_array]=amplitude
                continue
            else:
                continue
        return 0

    def get_position_pulse_in_waveform(self,time_enter_defect,dt):
        return int((dt/self.m_acquisition.m_dt))

    def get_amplitude(self,ball:RollingElement,interval_underball:tuple):
        # test if I am leaving the first interval
        pos_current_contact_interval=self.m_bearing.m_defect.\
                m_x_pos_filtered[interval_underball[0]]
        if interval_underball[0]-1>=0:
            pos_previous_contact_interval=self.m_bearing.m_defect.\
                    m_x_pos_filtered[interval_underball[0]-1]+\
                    self.m_bearing.m_defect.\
                    m_lambda_filtered[interval_underball[0]-1]
            amplitude=self.m_gamma*(pos_current_contact_interval\
                    -pos_previous_contact_interval)
            return amplitude
        else:
            amplitude=self.m_gamma*(pos_current_contact_interval)
            return amplitude


    def find_interval_under_ball(self,ball:RollingElement,j):
        for k in range(len(self.m_bearing.m_defect.m_x_pos_filtered)):
            ball_position=ball.m_x_pos_in_defect
            begin_interval=self.m_bearing.m_defect.m_x_pos_filtered[k]
            end_interval=self.m_bearing.m_defect.m_x_pos_filtered[k]+\
                    self.m_bearing.m_defect.m_lambda_filtered[k]

            if(begin_interval<ball_position and ball_position<end_interval):
                if k not in ball.m_index_interval_touched:
                    ball.m_index_interval_touched.append(k)
                    return (k,self.m_bearing.m_defect.m_index_filtered[k])
                else: continue
            if(begin_interval==self.m_bearing.m_defect.m_L
                    and begin_interval<ball_position):
                return (k,self.m_bearing.m_defect.m_index_filtered[k])
        return 0


    def start(self):
        time_start=time.time()
        for t in self.m_threads:
            t.start()
        for t in self.m_threads:
            t.join()
        noise = np.random.normal(0,
                self.m_acquisition.m_noise*max(self.m_acquisition.m_waveform),
                self.m_acquisition.m_waveform.shape)
        self.m_acquisition.m_waveform+=noise
        print("simulation completed in "+str(time.time()-time_start)+"s.")

    def get_results(self,format:str,file_name='results.png',
            title="Simulated spectrum"):
        fft_res=self.m_acquisition.get_fft()
        x=fft_res[0][:int(self.m_acquisition.m_frequency/10)]
        y=fft_res[1][:int(self.m_acquisition.m_frequency/10)]
        if format=='as_array':
            print("output formated as array, it's going to be ugly but you \
            asked for it")
            np.set_printoptions(threshold=sys.maxsize)
            print(self.m_acquisition.m_spectrum)

        elif format=='as_file':
            print('output formated as file')
        elif format=='as_graph':
            import matplotlib.pyplot as plt
            plt.title(title)
            plt.xlabel("Freq (Hz)")
            plt.ylabel("Amplitude")
            plt.plot(x, y, color ="red")
            plt.savefig(file_name)
        elif format=='show':
            import matplotlib.pyplot as plt
            plt.title(title)
            plt.xlabel("Freq (Hz)")
            plt.ylabel("Amplitude")
            plt.plot(x, y, color ="red")
            plt.show()
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





