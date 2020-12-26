#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fit of the intensity as a function of the thickness of the filter
    with an exponential function
    n(d) = n_u + n_0 exp(-alpha d) 
"""


import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# Define the exponential function to be fitted
def exp_dec(d, n_u, n_0, alpha):
    return n_u + n_0 * np.exp(-alpha * d) 


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

# Optimising the parameters
popt, pcov = scipy.optimize.curve_fit(exp_dec, d, n, 
                            # Initial guess of the parameters
                            [40, 2200, 10], sigma=dn)
# Unpacking the parameters
n_u, n_0, alpha = popt

# Computing the uncertainty from the covariance matrix
d_n_u, d_n_0, d_alpha = np.sqrt(np.diag(pcov))

# Printing the values of the optimised parameters
print('Result of the optimisation')
print(f'n_u = ({n_u:4.0f} +- {d_n_u:2.0f}) 1/min.')
print(f'n_0 = ({n_0:4.0f} +- {d_n_0:2.0f}) 1/min.')
print(f'alpha = ({alpha:4.0f} +- {d_alpha:2.0f}) 1/mm.')

# initialise a figure and an axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Filter thickness d [mm]')
ax.set_ylabel('Intensity n [1/min]')
ax.set_yscale('log')
ax.grid()

# Plot the fitted function
d_fit = np.linspace(np.min(d), np.max(d), 500)
n_fit = exp_dec(d_fit, n_u, n_0, alpha)
ax.plot(d_fit, n_fit, '-', zorder=2)

# Plot the measurements with the error bars
ax.errorbar(d, n, yerr=dn, fmt='.', capsize=2)
plt.show()

