#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Numerical Integration of the normal distribution with the midpoint rule
"""

import math

sigma = 0.5         # Standard deviation
x_max = 3           # Integration domain from -x_max to +x_max
dx = 0.01           # Width of the Integration interval


def f(x):
    """ Normal distribution. Standard deviation: sigma, Mean: 0
    """
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * math.exp(- x**2/(2 * sigma**2))


x = -x_max
p = 0.
while x < x_max:
    p += f(x + dx/2) * dx
    x += dx

print(p)