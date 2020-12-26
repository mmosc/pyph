#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Calculating Mean, Standard Deviation and of the Standard Error of the Mean.
    Data related to the oscillation period of a pendulum.
"""

import math
import numpy as np


# Measured values of the period [s]
T = np.array([2.05, 1.99, 2.06, 1.97, 2.01, 
              2.00, 2.03, 1.97, 2.02, 1.96])

# Number of measures
n  = T.size

# Calculating the mean
mean = 0
for x in T:
    mean += x
mean /= n

# Calculating the Standard Deviation
sigma = 0
for x in T:
    sigma += (x - mean) **2
sigma = math.sqrt(sigma / (n - 1))

# Calculating the Standard error of the mean
delta_T = sigma / math.sqrt(n)

print(f'Mean:                         <T> = {mean:.10f} s')
print(f"Standard Deviatio :             \u03C3 = {sigma:.10f} s")
print(f'Standard Error of the Mean:    \u0394T = {delta_T:.10f} s')


# With numpy
mean_np = np.mean(T)
sigma_np = np.std(T, ddof=1)
delta_T_np = sigma / math.sqrt(T.size)

print(f'Mean numpy:                         <T> = {mean_np:.10f} s')
print(f"Standard Deviatio numpy :             \u03C3 = {sigma_np:.10f} s")
print(f'Standard Error of the Mean numpy:    \u0394T = {delta_T_np:.10f} s')


print(f'Mean:                          {np.abs(mean_np-mean)/mean:.2f} s')
print(f"Standard Deviatio :              {np.abs(sigma_np-sigma)/sigma:.2f} s")
print(f'Standard Error of the Mean:     {np.abs(delta_T_np-delta_T)/delta_T:.2f} s')





















