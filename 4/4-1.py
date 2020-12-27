"""2D free fall """

import numpy as np
import matplotlib.pyplot as plt
import math

h = 10.0                 # Initial height [m]
v_throw = 5.0                # Initial velocity [m/s]
alpha_deg = [30., 60., 80.]         # Throwing angle [°]
g = 9.81                 # Gravitational acceleration [m/s²]


def trajectory(alpha_deg, rad=False):
    if rad==True: alpha=alpha_deg
    else:# Convert the angle to radians
        alpha = math.radians(alpha_deg)
    
    # Store the vectors as 1D arrays
    r0 = np.array([0, h])
    v0 = np.array([v_throw * math.cos(alpha), v_throw * math.sin(alpha)])
    a = np.array([0, -g])
    
    # Compute the time at which the object hits the floor 
    t_e = v0[1] / g + math.sqrt((v0[1] / g)**2 + 2 * r0[1] / g)
    
    # initialise an array of times at which evaluating x and y to be plotted
    t = np.linspace(0, t_e, 1000)
    # Broadcasting needed to copute the tensorial product
    t = t.reshape(-1, 1)
    
    # Compute the position at each time of the array t
    return r0 + v0 * t + 0.5 * a * t**2
    
# Initialise the plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.grid()

for angle in alpha_deg:
    # Compute the trajectory
    r = trajectory(angle)
    
    # Plot the trajectory
    ax.plot(r[:, 0], r[:, 1])
    
    # Show the plot
plt.show()