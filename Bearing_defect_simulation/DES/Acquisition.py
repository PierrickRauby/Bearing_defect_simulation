import sys
import math
import numpy as np
from typing import Tuple

class Acquisition(object):
    """
    Acquisition class, represents the simulation time discretization
    """
    def __init__(self,a_duration:float=1,a_frequency:float=20000,
            a_noise:float=0.1):
        self.m_duration=a_duration # duration of the acquisition in (s)
        self.m_frequency=a_frequency # frequency of acquisition in (Hz)
        self.m_dt=1/a_frequency #time between 2 sampling point 1/m_frequency (s)
        self.m_noise=a_noise #noise parameter in the waveform
        # Atttributes relative to the vibration signal
        self.m_waveform_len=round(self.m_duration*self.m_frequency)
        self.m_waveform=np.zeros(self.m_waveform_len)
        self.m_spectrum=np.array([])

    def get_fft(self):
        self.m_spectrum=self.generate_fft()
        return self.m_spectrum

    def generate_fft(self):
        # This is not the best FFT ever but it does the job
        #ref:https://pythontic.com/visualization/signals/fouriertransform_fft 
        fourierTransform = np.fft.fft(self.m_waveform)/\
                len(self.m_waveform)           # Normalize amplitude
        fourierTransform = fourierTransform[range(int(len(self.m_waveform)/\
                2))] # Exclude sampling frequency
        tpCount     = len(self.m_waveform)
        values      = np.arange(int(tpCount/2))
        timePeriod  = tpCount/self.m_frequency
        frequencies = values/timePeriod
        return (frequencies,abs(fourierTransform))

    def get_info(self):
        print("################# ACQUISITION PARAM  ############## ")
        print("#")
        print("#  Duration: "+str(self.m_duration)+"s")
        print("#  Frequency: "+str(self.m_frequency)+"Hz")
        print("#  Time resolution:"+str(round(1000000*self.m_dt)/1000000)+"s")
        print("#  Number of signal's point:"+str(self.m_waveform_len))
        print("#")
