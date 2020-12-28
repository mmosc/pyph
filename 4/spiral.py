""" Spiral motion with constant angular velocity. Numerical simulation
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d


# define a 3d arrow
class Arrow3D(mpl.patches.FancyArrowPatch):

    def __init__(self, posA, posB, *args, **kwargs):
        super().__init__(posA[0:2], posB[0:2], *args, **kwargs)
        self._pos = np.array([posA, posB])

    def set_positions(self, posA, posB):
        self._pos = np.array([posA, posB])

    def draw(self, renderer):
        p = mpl_toolkits.mplot3d.proj3d.proj_points(self._pos,
                                                    renderer.M)
        super().set_positions(*p[:, 0:2])
        super().draw(renderer)


R = 3.0                 # radius [m]
T = 8.0                 # period[s]
dt = 0.05                                   # Time step[s]
omega = 2 * np.pi / T    # angular velocity
vz = 0.5                 # velocity along z [m/s]


# Array of time steps dt between 0 and T
t = np.arange(0, T, dt)

# Empty array for the position of the object
r = np.empty((t.size, 3))

# Calculate the position of the point for each timestep
r[:, 0] = R * np.cos(omega * t)
r[:, 1] = R * np.sin(omega * t)
r[:, 2] = vz * t

# Calculate numerically the velocity and the acceleration vectors 
v = (r[1:, :] - r[:-1, :]) / dt
a = (v[1:, :] - v[:-1, :]) / dt

# Initialise the figure and the axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d',
                     elev=40, azim=45)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')
#ax.set_xlim(-4, 4)
#ax.set_ylim(-4, 4)
#ax.set_aspect('equal')
ax.grid()

# Plot the trajectory
traj, = ax.plot(r[:, 0], r[:, 1], r[:, 2], linewidth=0.7)

# Initialise a point tracking the position of the object
point, = ax.plot([], [], [], 'o', color='red')

# Velocity and acceleration arrows
style = mpl.patches.ArrowStyle.Simple(head_length=6,
                                      head_width=3)
arrow_v = Arrow3D((0, 0, 0), (0, 0, 0), 
                                      color='red', 
                                      arrowstyle=style)
arrow_a = Arrow3D((0, 0, 0), (0, 0, 0), 
                                      color='black', 
                                      arrowstyle=style)

# Function to update the animation
def update(n):
    # Update the velocity vector
    if n < v.shape[0]:
        arrow_v.set_positions(r[n], r[n] + v[n])
        
    # Update the acceleration vector
    if n < a.shape[0]:
        arrow_a.set_positions(r[n], r[n] + a[n])
        
    # Update the position of the point
    point.set_data(r[n, 0:2])
    point.set_3d_properties(r[n,2])
    
    return point, arrow_v, arrow_a

# Initialise the animation object and start the animation
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size)


plt.show()










