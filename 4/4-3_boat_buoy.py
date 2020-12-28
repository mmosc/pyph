"""Boat pointing to a buoy not taking into account the velocity of the 
    water stream.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


# Initial position (x, y) of the boat [m].
r0_boat = np.array([-10, 2.0])

# Position (x, y) des Zieles [m].
r_buoy = np.array([0.0, 0.0]) 
v0_stream = np.array([0.0, -2.5])                 # Stream velocity [m/s]
v0_boat = 3.0                                   # Module of dog velocity [m/s]

t_max = 500                                    # Maximal duration of the simulation[s]
dt = 0.01                                    # Time step[s]

# Stop the simulation if the distance between dog and man is smaller than epsilon.
epsilon = v0_boat * dt

# Define lists storing the results of the simulation
t = [0]
r_boat = [r0_boat]
v_boat = []

# Loop of the simulation
while True:
    # Calculate the velocity of the dog. This is done before the break since
    # the velocity has an entry less compared to the positions
    delta_r = r_buoy - r_boat[-1]
    v = v0_boat * delta_r/np.linalg.norm(delta_r) + v0_stream
    v_boat.append(v)
    
    # break the loop if either the dog and the man are closer than epsilon 
    # or if we exceed the iteration limit
    if (np.linalg.norm(delta_r) < epsilon ) or (t[-1] > t_max):
        break
    
    # Calculate the new position of man and dog
    r_boat.append(r_boat[-1] + dt * v)
    
    # Calculate the new time
    t.append(t[-1] + dt)
    
# Convert the lists to array AFTER the loop, since 
# during the loop we need the append module
t = np.array(t)
r_boat = np.array(r_boat)
v_boat = np.array(v_boat)

# Compute the acceleration of the dog (leave out initial and final velocity)
# through linear interpolation
a_boat = (v_boat[1:, :] - v_boat[:-1, :]) / dt

# Initialise the figure and the axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-11, 1)
ax.set_ylim(-5, 3)
ax.set_aspect('equal')
ax.grid()


# Initialise an empty plot for the trajectory of the dog
plot, = ax.plot([], [])

# Initialise two empty point-plots for the position of the dog and of the man
boat, = ax.plot([], [], 'o', color='blue')
buoy, = ax.plot([r_buoy[0]], [r_buoy[1]], 'o', color='red')

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
    arrow_v.set_positions(r_boat[n], r_boat[n] + v_boat[n])
    
    # Define the origin and end of the acceleration vector
    arrow_a.set_positions(r_boat[n], r_boat[n] + a_boat[n])

    # Update the position of dog and man
    boat.set_data(r_boat[n])
    
    # Plot the trajectory of the dog till the current time 
    plot.set_data(r_boat[:n + 1, 0], r_boat[:n + 1, 1])
    
    return boat, arrow_v, arrow_a, plot

# Initialise the animation object and start the animation
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True)



plt.show()










