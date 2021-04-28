# Bearing_defect_simulation
A python library to create vibration signal for bearing defects. 
This as been developped and tested using python3.9.1
[![Python 3.6](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-391/)

## How to use it? 
First clone it:
```
git clone https://github.gatech.edu/prauby3/Bearing_defect_simulation.git
cd Bearing_defect_simulation
```
Then install the requirements:
``` 
python3 -m pip install -r requirements.txt
```

Then you can run the simulation by doing:
```
python3 simulation . py
```

This will run the default settings for the simulation, the simulation.py code also come with and commandline argument parser with the following option:


| Command line argument |       |                                                                           |                       |
|:---------------------:|-------|---------------------------------------------------------------------------|-----------------------|
| Argument              | Type  | Fonction                                                                  | Default               |
| --n                   | int   | Number of rolling elements                                                | 16                    |
| --dP                  | float | Pitch diameter of the bearing (mm)                                        | 71.501                |
| --race                | str   | Race affected by the defect either "inner" or "outer"                     | "outer"               |
| --rpm                 | int   | Rotational speed of the cage one relative to the other (rpm)              | 2000                  |
| --dB                  | float | The Rolling Element Diameter (mm)                                         | 8.4074                |
| --theta               | float | The contact angle of the bearing (deg)                                    | 15.17                 |
| --L                   | float | The length of the defect region (mm)                                      | 3.8                   |
| --N                   | int   | The number of interval of the defect.                                     | 5                     |
| --a_lambda            | list  | The different lengths of the intervals representing the defect (mm)       | [0.7,0.7,0.8,0.8,0.8] |
| --a_delta             | list  | The different depth of the intervals representing the defect (mm)         | [0.5,0,0.5,0,0.7]     |
| --duration            | float | The duration of the simulation (s)(not the time the program takes to run) | 1                     |
| --frequency           | float | The time resolution of the simulation (Hz)                                | 20000                 |
| --noise               | float | The ration of noise to add in the simulation [0.0,0.9]                    | 0.1                   |

__Note1:__ The duration command-line argument does not represent the program’s runtime but the duration for which the ball roll in the bearing.

__Note2:__ When playing with the different command-line arguments, one should be very careful that what the program is asked for actually makes sense. This program is intended to simulate actual situations, and the validity of the argument does not check. For example, the program will try to run (and will undoubtedly crash) if one asks for a defect length longer than the circumference of the race or a negative number of rolling elements, but it does not make any sense in real life. The time resolution and duration of acquisition should be chosen carefully to satisfy the Nyquist–Shannon sampling theorem as the simulation engine behaves like if it is sampling the analog vibration generated by the ball rolling on the races.



## Structure of the Project
The repository contains the following folders:
  - Bearing defect simulation: It contains 2 folders:
    - Bearing This folder contains the classes:
      - Bearing implementation of the bearing object as in 4
      - Defect implementation of the 6
      - RollingElement implementation of the 5
    - DES The folder where the simulation engine lives with in the class Simulation, 2 other classes were also
added:
      - Acquistion which manages the time fonction and time interval.
      -  Signal The Signal class is where the results of the simulation are stored.
      - test contains the test for validation of the project. When run, each code will to recreatese one of the Figures 5,6 or 7. It also contains three .csv files that contain the data for 2 BPFO defects and one healthy signal from the NASA dataset.
- docs contains the different reports of the project
- requirements.txt: the requirement to install
- simulation.py the main code to run with command line argument if you want to test the project.
