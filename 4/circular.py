""" Circular motion with constant angular velocity. Numerical simulation
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


R = 3.0                 # radius [m]
T = 12.0                 # period[s]
dt = 0.02                                    # Time step[s]
omega = 2 * np.pi / T    # angular velocity

# Analytic solution
print(f'Spacial velocity:     {R*omega:.3f} m/s')
print(f'Centripetal acceleration:     {R*omega**2:.3f} m/s²')

# Array of time steps dt between 0 and T
t = np.arange(0, T, dt)

# Empty array for the position of the object
r = np.empty((t.size, 2))

# Calculate the position of the point for each timestep
r[:, 0] = R * np.cos(omega * t)
r[:, 1] = R * np.sin(omega * t)

# Calculate numerically the velocity and the acceleration vectors 
v = (r[1:, :] - r[:-1, :]) / dt
a = (v[1:, :] - v[:-1, :]) / dt

# Initialise the figure and the axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.grid()


# Initialise an empty plot for the trajectory of the dog
plot, = ax.plot([], [])

# Analytic curve
an_curve = ax.plot(r[:, 0], r[:, 1])

# Initialise two empty point-plots for the position of the dog and of the man
traj, = ax.plot([], [], 'o', color='blue')

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

    # Update the position of dog and man
    traj.set_data(r[n])
    
    # Plot the trajectory of the dog till the current time 
    plot.set_data(r[:n + 1, 0], r[:n + 1, 1])
    
    return traj, arrow_v, arrow_a, plot

# Initialise the animation object and start the animation
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True)

ax.text(0, 0.5, f'v = {R*omega:.3f} m/s',color='red')
ax.text(0, 0, f'a = {R*omega**2:.3f} m/s²')


plt.show()










