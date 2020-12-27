"""Radiodrome, i.e. Dog following man. The problem is not analytic and
    is approached numerically. Interpolation is linear and there is a 
    maximal integration time, for the case in which the human is 
    faster than the dog.
"""

import numpy as np
import matplotlib.pyplot as plt


r0_dog = np.array([0.0, 10.0])                 # Initial dog position  [m]
r0_man = np.array([0.0,  0.0])                 # Initial man position  [m]
v0_man = np.array([2.0,  0.0])                 # Initial man velocity [m/s]
v0_dog = 3.0                                   # Module of dog velocity [m/s]

t_max = 500                                    # Maximal duration of the simulation[s]
dt = 0.01                                    # Time step[s]

# Stop the simulation if the distance between dog and man is smaller than epsilon.
epsilon = v0_dog * dt

# Define lists storing the results of the simulation
t = [0]
r_dog = [r0_dog]
r_man = [r0_man]
v_dog = []