#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Simulation of the normal distribution. We want to test the central limit theorem
    We have a large number of measured values n_meas with n_distur independent sources of error
    each with its distribution. in the limit of n_disturb going to infinity, their sum
    should be distributed as a gaussian.
"""
import numpy as np
import math
import matplotlib.pyplot as plt


n_meas = 50000              # number of measured values
n_distur = 20                  # number of independent sources of error


# We simulate the sources of error. Each is lying in the interval [0,1[
# Since we have n_distur sources of error for each of the n_meas measurements
# we need to generate a n_meas x n_distur matrix
meas = np.random.rand(n_meas, n_distur)
meas = np.sum(meas, axis=1)


# Calculate the meaan and the standard deviation
mean = np.mean(meas)
sigma = np.std(meas)
def f(x, mean=mean, sigma=sigma):
    """ Normal distribution. Standard deviation: sigma, Mean: mean
    """
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * np.exp(- (x - mean)**2/(2 * sigma**2))

# Initialise a figure 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Measured value')
ax.set_ylabel('Probability')
ax.grid()

# Plot a histogram of the simulated values
p, bins, patches = ax.hist(meas, bins=51, density=True)

# Calculate the values of the normal distribution at the boundaries of the 
# histogram bins and plot them
ax.plot(bins, f(bins))

# Display the plot
plt.show()
