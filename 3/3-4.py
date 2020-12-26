#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fit of the drag force F as a function of the velocity v 
    with an power law of the type
    F(v) = b * np.abs(v)**n 
"""


import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# Define the exponential function to be fitted
def abs_pol(v, b, n):
    return b * np.abs(v)**n 


# Velocity and velocity error [m/s]
v = np.array([5.8, 7.3, 8.9, 10.6, 11.2])
dv = np.array([0.3, 0.3, 0.2, 0.2, 0.1])

# Measured force and error [N]
F = np.array([0.10, 0.15, 0.22, 0.33, 0.36])
dF = np.array([0.02, 0.02, 0.02, 0.02, 0.02])

# Optimising the parameters
popt, pcov = scipy.optimize.curve_fit(abs_pol, v, F, 
                            sigma=dF)
# Unpacking the parameters
b, n = popt

# Computing the uncertainty from the covariance matrix
d_b, d_n = np.sqrt(np.diag(pcov))

# Printing the values of the optimised parameters
print('Result of the optimisation')
print(f'b = ({b:4.5f} +- {d_b:2.5f}) [N*s^n/m^n].')
print(f'n = {n:4.2f} +- {d_n:2.2f}.')

# initialise a figure and an axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Velocity v [m/s]')
ax.set_ylabel('Force F [N]')
#ax.set_yscale('log')
ax.grid()

# Plot the fitted function
v_fit = np.linspace(np.min(v), np.max(v), 500)
F_fit = abs_pol(v_fit, b, n)
ax.plot(v_fit, F_fit, '-', zorder=2)

# Plot the measurements with the error bars
ax.errorbar(v, F, xerr=dv, yerr=dF, fmt='.', capsize=2)
plt.show()

