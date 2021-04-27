import numpy as np
import sys
sys.path.append('../')
from Bearing_defect_simulation.Bearing.Bearing import Bearing
from Bearing_defect_simulation.DES.Simulation import Simulation
from Bearing_defect_simulation.DES.Acquisition import Acquisition

my_bearing=Bearing()
my_acquisition=Acquisition()
my_simulation=Simulation(my_bearing,my_acquisition)
# my_simulation.start()
my_simulation.get_results('as_file')
