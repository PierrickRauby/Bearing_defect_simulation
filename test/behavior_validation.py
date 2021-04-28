import numpy as np
import sys
from PIL import Image
sys.path.append('../')
from Bearing_defect_simulation.Bearing.Bearing import Bearing
from Bearing_defect_simulation.DES.Simulation import Simulation
from Bearing_defect_simulation.DES.Acquisition import Acquisition

def main():
    print("################# Face validation  ############## ")
    print("# This test runs the simulation twice for the ")
    print("#  same bearing as for the Nasa dataset, chaging")
    print("#  the rpm we want to validate that the defect")
    print("#  frequency increase with the rpm:")
    print("#        1- rotional speed: 2000 rpm")
    print("#        2- rotional speed: 1000 rpm")
    print("# Expected results:")
    print("#    The simulated spectruum at 1000rpm should")
    print("#     show more peaks as the frequency is divided")
    print("#     by 2 compared to the simulation at 2000rpm")
    print("################################################### ")
    my_bearing=Bearing(a_rpm=2000)
    my_acquisition=Acquisition(a_noise=0.0)
    my_simulation=Simulation(my_bearing,my_acquisition)
    my_simulation.start()
    my_simulation.get_results(format='as_graph',file_name='2000_rpm.png',
            title='Simulated 2000rpm')
    my_bearing=Bearing(a_rpm=1000)
    my_acquisition=Acquisition(a_noise=0.0,a_frequency=10000)
    my_simulation=Simulation(my_bearing,my_acquisition)
    my_simulation.start()
    my_simulation.get_results(format='as_graph',file_name='1000_rpm.png',
            title='Simulated 1000rpm')
    f1 = Image.open("2000_rpm.png")
    f2 = Image.open("1000_rpm.png")
    get_concat_h(f1, f2).save('comparison.png')
    f2.close()
    f1.close()
    f3 = Image.open("comparison.png").show()

def get_concat_h(im1, im2):
    # https://note.nkmk.me/en/python-pillow-concat-images/
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

if __name__ == '__main__':
    main()

