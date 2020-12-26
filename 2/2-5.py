#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0 1
0 2.8
1 3.3
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_field(x, y, cycled=True):
    """ Plots the corners of the field as well as its boundaries.
    The function accepts as inputs two lists with the x and y coordinates
    of the corners respectively. The values must be cycled 
    (i.e. first element of the array equals last element)
    """
    
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, 'ro', zorder=2)
    
    if cycled==False:
        x.append(x[0])
        y.append(y[0])
        
    ax.plot(x, y, 'b-', zorder=1)
    plt.show()


def surface(x, y, cycled=True):
    """
    Calculates the surface of a polygon using the gaussian 
    trapezoidal formula:
            A = abs(sum( (y_i+ y_{i+1})(x_i-x_{i+1}) ) )
    The function accepts as inputs two lists with the x and y coordinates
    of the corners respectively. The values must be cycled 
    (i.e. first element of the array equals last element)
    Returns the value of the surface
    """
    
    
    x = np.array(x)
    x_diff = x - np.roll(x, 1)
    
    y = np.array(y)    
    y_sum = y + np.roll(y, 1)
    
    
    return np.abs(x_diff@y_sum)/2

x = [0.0, 0.0, 1.0, 2.2, 2.8, 3.8, 4.6, 5.7, 6.4, 7.1, 7.6, 7.9, 7.9, 0.0]
y = [1.0, 2.8, 3.3, 3.5, 3.4, 2.7, 2.4, 2.3, 2.1, 1.6, 0.9, 0.5, 0.0, 1.0]

plot_field(x, y)
A = surface(x, y)

print(f'The area is {A:5.4f}.')