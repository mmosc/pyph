#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Calculating the percentual of measures lying in the intervall [1.95, 2.05]
    assuming that we repeat the measurement always in the same conditions.
    Data related to the oscillation period of a pendulum.
"""

import math
import numpy as np
import scipy.integrate

def f(x, mean, sigma):
    """ Normal distribution. Standard deviation: sigma, Mean: 0
    """
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * math.exp(- (x - mean)**2/(2 * sigma**2))

# Measured values of the period [s]
T = np.array([2.05, 1.99, 2.06, 1.97, 2.01, 
              2.00, 2.03, 1.97, 2.02, 1.96])
x_min = 1.95
x_max = 2.05


# With numpy
mean_np = np.mean(T)
sigma_np = np.std(T, ddof=1)
delta_T_np = sigma / math.sqrt(T.size)


# Integrate using QUADPACK. Returns the integral .
p, err = scipy.integrate.quad(f, x_min, x_max, args=(mean_np, sigma_np))


print(f'{p*100:.1f}% of the measurements are expected between {x_min:.2f} and {x_max:.2f}.')




















