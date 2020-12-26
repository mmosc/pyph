#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Half-logarithmic dilution of the measured values
"""


import numpy as np
import matplotlib.pyplot as plt


# Thickness of the filter [mm]
d = np.array([0.000, 0.029, 0.039, 0.064, 0.136, 0.198, 
              0.247, 0.319, 0.419, 0.511, 0.611, 0.719, 
              0.800, 0.900, 1.000, 1.100, 1.189])

# Measured intensities [counts / minute]
n = np.array([2193, 1691, 1544, 1244, 706, 466, 
              318, 202, 108, 80, 52, 47, 
              45, 46, 47, 42, 43], dtype=np.float)

# Uncertainty on the measured intensities
dn = np.array([47, 41, 39, 35, 26, 22,
               18, 14, 10, 9, 7, 7, 
               7, 7, 7, 7, 7], dtype=np.float)

# initialise a figure and an axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Filter thickness d [mm]')
ax.set_ylabel('Intensity n [1/min]')
ax.set_yscale('log')
ax.grid()

# Plot the measurements with the error bars
ax.errorbar(d, n, yerr=dn, fmt='.', capsize=2)
plt.show()

