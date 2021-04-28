import numpy as np
from scipy import fft,ifft

class Signal(object):
    """
    Signal class
    """
    def __init__(self,a_waveform_len:int,a_waveform:np.ndarray,
            a_time_resolution:float,a_spectruum:np.ndarray):
        self.m_waveform_len=a_waveform_len
        self.m_waveform=np.zeros(self.m_waveform_len)
        self.m_time_resolution=a_time_resolution
        self.m_spectrum=np.array([])

    def get_fft(self):
        # not usefull, for futur use
        self.m_spectrum=fft(self.m_waveform_len)
        return self.m_spectrum

    def get_ifft(self):
        # not usefull, for futur use
        print(shape(self.m_spectrum))
