""" Here is our pendulum situation. For some reason we are getting
an index out of bounds error during the while loop but I can't figure
out why. We are also still having issues with the time step even though
we feel as though it should be working (compared to the model)
This code was made by Grace Anderson and Bowton Eaves
and so far has taken approximately 7 hours.
"""
import math
import numpy as np
angle = []
vel = []
acc = []
length = .25
angNext = math.pi / 6
i = 1
time = np.linspace(0,10,10)
angNext = 0
velNext = 0
accNext = 0

def print_system(time,angle,velocity, acceleration):
    print("TIME:     ", time)
    print("ANGLE: ", angle)
    print("VELOCITY: ", velocity)
    print("ACCELERATION: ", acceleration, "\n")

def update_system(acc,angle,vel,time1,time2):
    dt = time2-time1
    angleNext = angle+vel*dt
    velNext = vel+acc*dt
    accNext = (-9.81 * math.sin(angleNext))/length
    return angleNext, velNext, accNext

while i < len(time)-1:
    angleNext, velNext, accNext = update_system(acc[i],angle[i-1], vel[i-1],time[i-1],time[i])
    acc.append(accNext)
    vel.append(velNext)
    angle.append(angNext)
    print_system(time[i], angle[i],vel[i], acc[i])
    i = i + 1