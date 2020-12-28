"""Radiodrome, i.e. Dog following man. The problem is not analytic and
    is approached numerically. Interpolation is linear and there is a 
    maximal integration time, for the case in which the human is 
    faster than the dog.
"""

import numpy as np
import matplotlib.pyplot as plt


r0_dog = np.array([0.0, 10.0])                 # Initial dog position  [m]
r0_man = np.array([0.0,  0.0])                 # Initial man position  [m]
v0_man = np.array([2.0,  0.0])                 # Initial man velocity [m/s]
v0_dog = 3.0                                   # Module of dog velocity [m/s]

t_max = 500                                    # Maximal duration of the simulation[s]
dt = 0.01                                    # Time step[s]

# Stop the simulation if the distance between dog and man is smaller than epsilon.
epsilon = v0_dog * dt

# Define lists storing the results of the simulation
t = [0]
r_dog = [r0_dog]
r_man = [r0_man]
v_dog = []

# Loop of the simulation
while True:
    # Calculate the velocity of the dog. This is done before the break since
    # the velocity has an entry less compared to the positions
    delta_r = r_man[-1] - r_dog[-1]
    v = v0_dog * delta_r/np.linalg.norm(delta_r)
    v_dog.append(v)
    
    # break the loop if either the dog and the man are closer than epsilon 
    # or if we exceed the iteration limit
    if (np.linalg.norm(delta_r) < epsilon ) or (t[-1] > t_max):
        break
    
    # Calculate the new position of man and dog
    r_dog.append(r_dog[-1] + dt * v)
    r_man.append(r_man[-1] + dt * v0_man)
    
    # Calculate the new time
    t.append(t[-1] + dt)
    
# Convert the lists to array AFTER the loop, since 
# during the loop we need the append module
t = np.array(t)
r_dog = np.array(r_dog)
r_man = np.array(r_man)
v_dog = np.array(v_dog)

# Compute the acceleration of the dog (leave out initial and final velocity)
# through linear interpolation
a_dog = (v_dog[1:, :] - v_dog[:-1, :]) / dt

# Initialise the figures
fig = plt.figure(figsize=(10, 3))
fig.set_tight_layout(True)

# Plot the trajectory of the dog
ax1 = fig.add_subplot(1, 3, 1)
ax1.set_xlabel('x [m]')
ax1.set_ylabel('y[m]')
ax1.set_aspect('equal')
ax1.grid()
ax1.plot(r_dog[:,0], r_dog[:,1])
ax1.plot(r_man[:,0], r_man[:,1])

# Plot the distance between man and dog. The notm must be calculated along the
# axis=1 since the rows are the time slices
ax2 = fig.add_subplot(1, 3, 2)
ax2.set_xlabel('t [s]')
ax2.set_ylabel('Distance [m]')
ax2.grid()
ax2.plot(t, np.linalg.norm(r_dog - r_man, axis=1))

# Norm of the acceleration of the dog+
ax3 = fig.add_subplot(1, 3, 3)
ax3.set_xlabel('t [s]')
ax3.set_ylabel('Acceleration [m/s²]')
ax3.grid()
ax3.plot(t[1:], np.linalg.norm(a_dog, axis=1))

# show the plot
plt.show()













