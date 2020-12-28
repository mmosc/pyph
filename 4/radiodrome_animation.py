"""Radiodrome, i.e. Dog following man. The problem is analytic but
    is approached numerically. Interpolation is linear and there is a 
    maximal integration time, for the case in which the human is 
    faster than the dog.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


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

# Initialise the figure and the axis object
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_xlim(-0.2, 15)
ax.set_ylim(-0.2, 10)
ax.set_aspect('equal')
ax.grid()


# Initialise an empty plot for the trajectory of the dog
plot, = ax.plot([], [])

# Analytic curve
k =  v0_man[0]/v0_dog
y_analyt = np.linspace(0, r0_dog[1], 500)
x_analyt = 0.5 * r0_dog[1] * ( ( 1 - ( y_analyt / r0_dog[1] )**(1 - k) ) / (1 - k) - ( 1 - ( y_analyt / r0_dog[1] )**(1 + k) ) / (1 + k) )
an_curve = ax.plot(x_analyt, y_analyt)

# Initialise two empty point-plots for the position of the dog and of the man
dog, = ax.plot([], [], 'o', color='blue')
man, = ax.plot([], [], 'o', color='red')

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
    arrow_v.set_positions(r_dog[n], r_dog[n] + v_dog[n])
    
    # Define the origin and end of the acceleration vector
    arrow_a.set_positions(r_dog[n], r_dog[n] + a_dog[n])

    # Update the position of dog and man
    dog.set_data(r_dog[n])
    man.set_data(r_man[n])
    
    # Plot the trajectory of the dog till the current time 
    plot.set_data(r_dog[:n + 1, 0], r_dog[:n + 1, 1])
    
    return dog, man, arrow_v, arrow_a, plot

# Initialise the animation object and start the animation
ani = mpl.animation.FuncAnimation(fig, update, interval=30,
                                  frames=t.size, blit=True)



plt.show()










