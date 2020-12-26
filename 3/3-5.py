#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Fit of the amplitude A as a function of the frequency f
    A(f) = A_0 * f_0**2 / np.sqrt( ( f**2 - f_0**2 )**2 + ( deltaf / np.pi )**2 )
"""


import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# Define the amplitude function to be fitted
def amplitude(f, A_0, f_0, deltaf):
    return A_0 * f_0**2 / np.sqrt( ( f**2 - f_0**2 )**2 + ( deltaf * f / np.pi )**2 )


# frequency [Hz]
f = np.array([0.2, 0.5, 0.57, 0.63, 0.67,
              0.71, 0.80, 1.00, 1.33])

# Measured amplitude [cm]
A = np.array([0.84, 1.42, 1.80, 2.10, 2.22,
              2.06, 1.45, 0.64, 0.30])
dA = np.array([0.04, 0.07, 0.09, 0.11, 0.11,
               0.10, 0.08, 0.03, 0.02])

# Optimising the parameters
popt, pcov = scipy.optimize.curve_fit(amplitude, f, A, 
                            [0.8, 0.7, 0.3], sigma=dA)
# Unpacking the parameters
A_0, f_0, deltaf = popt

# Computing the uncertainty from the covariance matrix
d_A_0, d_f_0, d_deltaf= np.sqrt(np.diag(pcov))

# Printing the values of the optimised parameters
print('Result of the optimisation')
print(f'A_0 = ({A_0:4.2f} +- {d_A_0:2.2f}) cm.')
print(f'f_0 = ({f_0:4.3f} +- {d_f_0:2.3f}) Hz.')
print(f'deltaf = ({deltaf:4.2f} +- {d_deltaf:2.2f}) 1/s.')

# initialise a figure and an axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Frequency f [Hz]')
ax.set_ylabel('Amplitude A [cm]')
#ax.set_yscale('log')
ax.grid()

# Plot the fitted function
f_fit = np.linspace(np.min(f), np.max(f), 500)
A_fit = amplitude(f_fit, A_0, f_0, deltaf)
ax.plot(f_fit, A_fit, '-', zorder=2)

# Plot the measurements with the error bars
ax.errorbar(f, A, yerr=dA, fmt='.', capsize=2)
plt.show()

