import sys
import math
import numpy as np

class Acquisition(object):
    """
    Documentation TOD
    """
    def __init__(self,a_duration:float=1,a_frequency:float=20000):
        self.m_duration=a_duration # duration of the acquisition in (s)
        self.m_frequency=a_frequency # frequency of acquisition in (Hz)
        self.m_dt=1/a_frequency #time between 2 sampling point 1/m_frequency (s)
        #TODO: keep or remove the next line 
        # self.get_info()

        # Atttributes relative to the vibration signal
        self.m_waveform_len=round(self.m_duration*self.m_frequency)
        self.m_waveform=np.zeros(self.m_waveform_len)
        self.m_spectrum=np.array([])

    def get_fft(self):
        self.m_spectrum=fft(self.m_waveform_len)
        #TODO: Complete this function
        print("TODO: fonction to complete")
        return self.m_spectrum

    def get_ifft(self):
        #TODO: Complete this function
        print("TODO: fonction to implement")
        print(shape(self.m_spectrum))

    def get_info(self):
        print("################# ACQUISITION PARAM  ############## ")
        print("#")
        print("#  Duration: "+str(self.m_duration)+"s")
        print("#  Frequency: "+str(self.m_frequency)+"Hz")
        print("#  Time resolution:"+str(round(1000000*self.m_dt)/1000000)+"s")
        print("#  Number of signal's point:"+str(self.m_waveform_len))
        print("#")
        print("################################################### ")

