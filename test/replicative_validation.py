import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd
from PIL import Image
sys.path.append('../')
from Bearing_defect_simulation.Bearing.Bearing import Bearing
from Bearing_defect_simulation.DES.Simulation import Simulation
from Bearing_defect_simulation.DES.Acquisition import Acquisition

def main():
    print("################# Replicative validation  ############## ")
    print("# This test runs the simulation with the same parameters")
    print("#  as for the NASA experiment number 3. It is expected ")
    print("#  to see the frequency peak of the simulation to be ")
    print("#  present in the real spectrum. However, as we have no")
    print("#  ideas of the real shape of the defect and because we")
    print("#  modeled only one bearing as opposed to 4 in the NASA")
    print("#  data, the simuliation will not show all the peak")
    print("#  present in the real spectruum. This is an expected ")
    print("#  limitation of the model.")
    print("################################################### ")
    my_bearing=Bearing(a_rpm=2000)
    my_acquisition=Acquisition(a_frequency=20480,a_noise=0.2)
    my_simulation=Simulation(my_bearing,my_acquisition)
    my_simulation.start()
    my_simulation.get_results(format='as_graph',
            file_name='simulated_signal.png',title='Simulated Signal')
    plt.close()
    array=pd.read_csv('Nasa_Test3_Healthy.csv', sep=',',header=0).values
    fft_res=generate_fft(array)
    x=fft_res[0][:2000]
    y=fft_res[1][:2000]
    plt.title("NASA real data")
    plt.xlabel("Freq (Hz)")
    plt.ylabel("Amplitude")
    plt.plot(x, y, color ="blue")
    plt.savefig('Nasa_data.png')
    f1 = Image.open("simulated_signal.png")
    f2 = Image.open("Nasa_data.png")
    get_concat_h(f1, f2).save('replicative_validation.png')
    f2.close()
    f1.close()
    f3 = Image.open("replicative_validation.png").show()

def get_concat_h(im1, im2):
    # https://note.nkmk.me/en/python-pillow-concat-images/
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def generate_fft(array):
    #ref:https://pythontic.com/visualization/signals/fouriertransform_fft 
    fourierTransform = np.fft.fft(array)/20
    fourierTransform = fourierTransform[range(int(len(array)/\
            2))] # Exclude sampling frequency
    tpCount     = len(array)
    values      = np.arange(int(tpCount/2))
    timePeriod  = tpCount/20000
    frequencies = values/timePeriod
    return (frequencies,abs(fourierTransform))

if __name__ == '__main__':
    main()

