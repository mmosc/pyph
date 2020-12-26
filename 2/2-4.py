#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Animation der Funktion 
        f(x) = 4/pi * sum(sin((2k+1)x)/(2k+1), k=0, k=inf)
    Jeder schritt addiert ein summand der Fourier Reihe.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


# x-Range in which to plot
x = np.linspace(0, 2 * np.pi,200)
y = 0 * x

# Initialisation of the figure
#plt.clf()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('x')
ax.set_ylabel('f_n')
ax.grid()


plot,  = ax.plot(x, y)
text = ax.text(0, -1, '')


# The plotting function1
def plot_ft(n):
    y = 0 * x
    for i in range(n):
        # Update the function and the plot
        y = y + 4 * np.sin((2 * i + 1) * x)/(np.pi * (2 * i + 1))
        
        
        # update plot
        plot.set_ydata(y)
        
        
        # update text
        text.set_text(f'n = {n:5.0f}')
        
        
    return plot, text
  

# Initialise the animation

ani = mpl.animation.FuncAnimation(fig, plot_ft, 
                                          interval=300, blit=True)
    
# Starte die Animation.
plt.show()









