""" 
    Pendulum
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


L = 3.0                 # radius [m]
T = 3.47                 # period[s]
phi_0_grad = 10.              # Initial angle [°]
phi_0 = np.radians(phi_0_grad)


dt = 0.02                                    # Time step[s]
omega = 2 * np.pi / T    # angular velocity

# Array of time steps dt between 0 and T
t = np.arange(0, T, dt)

# Empty array for the angle of the pendulum
phi = phi_0 * np.cos( omega * t)

# Empty array for the position of the object
r = np.empty((t.size, 2))

# Calculate the position of the point for each timestep
r[:, 0] = L * np.sin(phi)
r[:, 1] = -L * np.cos(phi)

# Calculate numerically the velocity and the acceleration vectors 
v = (r[1:, :] - r[:-1, :]) / dt
a = (v[1:, :] - v[:-1, :]) / dt

# Initialise the figure and the axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-0.5 * L, 0.5 * L)
ax.set_ylim(-1.2 * L, 0.1 * L)
ax.set_aspect('equal')
ax.grid()


# Initialise an empty plot for the trajectory of the dog
plot, = ax.plot([], [])

# Initialise two empty point-plots for the position of the dog and of the man
traj, = ax.plot([], [], 'o', color='blue')
line, = ax.plot([0, 0], [0, 0], color='black', lw=0.5)

# Formatting the arrows for velocity and acceleration
style = mpl.patches.ArrowStyle.Simple(head_length=6,
                                      head_width=3)
arrow_v = mpl.patches.FancyArrowPatch((0,0), (0,0), 
                                      color='red', 
                                      arrowstyle=style)
arrow_a = mpl.patches.FancyArrowPatch((0,0), (0,0), 
                                      color='black', 
                                      arrowstyle=style)

# Add arrows to the plot
ax.add_artist(arrow_v)
ax.add_artist(arrow_a)

# Function to update the animation
def update(n):
    # Define the origin and end of the velocity vector
    arrow_v.set_positions(r[n], r[n] + v[n])
    
    # Define the origin and end of the acceleration vector
    arrow_a.set_positions(r[n], r[n] + a[n])

    # Update the position of pendulum and line
    traj.set_data(r[n])
    line.set_data([0, r[n, 0]], [0, r[n, 1]])
    
    # Plot the trajectory till the current time 
    plot.set_data(r[:n + 1, 0], r[:n + 1, 1])
    
    return traj, line, arrow_v, arrow_a, plot

# Initialise the animation object and start the animation
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True)

plt.show()









