""" 
   Man shooting at a monkey.
   monkey image: Primate Vectors by Vecteezy https://www.vecteezy.com/free-vector/primate
   hunter image: Steps Vectors by Vecteezy https://www.vecteezy.com/free-vector/steps
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


r0_monkey = np.array([3.0, 2.0])               # initial position of monkey [m]
r0_arrow = np.array([.0, .0])                # initial position of hunter[m]
dt = 0.001                                    # Time step[s]
v0 = 9.0
v0_vec =  (r0_monkey - r0_arrow) / np.linalg.norm(r0_monkey - r0_arrow) * v0                              # initial velocity of the arrow
g = 9.81                              # gravitational acceleration [m/s²]

T = r0_monkey[0] / v0_vec[0]               #duration of the simulation, i.e. time for the arrow to reach the monkey

# Array of time steps dt between 0 and T
t = np.arange(0, T, dt)

# Empty array for the position of the monkey and of the arrow
r_monkey = np.empty((t.size, 2))
r_arrow = np.empty((t.size, 2))

# Calculate the position of the monkey for each timestep
r_monkey[:, 0] = r0_monkey[0]
r_monkey[:, 1] = r0_monkey[1] - 0.5 * g * t**2

# Calculate the position of the arrow for each timestep
r_arrow[:, 0] = r0_arrow[0] + v0_vec[0] * t
r_arrow[:, 1] = r0_arrow[1] + v0_vec[1] * t - 0.5 * g * t**2


# Calculate numerically the velocity and the acceleration vectors (could also do it analytically)
v_arrow = (r_arrow[1:, :] - r_arrow[:-1, :]) / dt
a_arrow = (v_arrow[1:, :] - v_arrow[:-1, :]) / dt

# Initialise the figure and the axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-0.2, r0_monkey[0]+.2)
ax.set_ylim(-0.2, r0_monkey[1]+.2)
ax.set_aspect('equal')
ax.grid()


# Initialise an empty plot for the trajectory of the dog
traj_arrow, = ax.plot([], [], color='red')
traj_monkey, = ax.plot([], [], color='blue')

# Initialise two empty point-plots for the position of the dog and of the man
point_arrow, = ax.plot([], [], 'o', color='red')
point_monkey, = ax.plot([], [], 'o', color='blue')


#image of the monkey
monkey_image = mpl.offsetbox.OffsetImage(plt.imread('monkey.png'),
                                  zoom=0.15)
box_monkey = mpl.offsetbox.AnnotationBbox(monkey_image, r0_monkey, frameon=False)
ax.add_artist(box_monkey)

#image of the hunter
hunter_image = mpl.offsetbox.OffsetImage(plt.imread('hunter.png'),
                                  zoom=0.3)
box_hunter= mpl.offsetbox.AnnotationBbox(hunter_image, (0, 0), frameon=False)
ax.add_artist(box_hunter)

# Function to update the animation
def update(n):
    # Update the position of arrow and monkey
    point_arrow.set_data(r_arrow[n])
    box_monkey.xybox = (r_monkey[n])

    
    # Plot the trajectory of the dog till the current time 
    traj_arrow.set_data(r_arrow[:n + 1, 0], r_arrow[:n + 1, 1])
    traj_monkey.set_data(r_monkey[:n + 1, 0], r_monkey[:n + 1, 1])

    
    return point_arrow, box_monkey, traj_arrow, traj_monkey

# Initialise the animation object and start the animation
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True,
                                  repeat_delay=1000)


plt.show()




