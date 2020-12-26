#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Numerical Integration of the normal distribution with the QUADPACK library
"""

import math
import scipy.integrate

sigma = 0.5         # Standard deviation
x_max = 3           # Integration domain from -x_max to +x_max


def f(x):
    """ Normal distribution. Standard deviation: sigma, Mean: 0
    """
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * math.exp(- x**2/(2 * sigma**2))



# Integrate using QUADPACK. Returns the integral and an estimate of 
# the absolute error.
p, err = scipy.integrate.quad(f, -math.inf, math.inf)


print(f'Result of the integration: {p}')
print(f'Relative Error of the integration: {(p-1)*100}%')
print(f'Estimate of the integration: {err}')