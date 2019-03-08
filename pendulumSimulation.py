import math
import matplotlib.pyplot as plt
import numpy as np
angle = [math.pi / 6]
vel = [0]
length = 1
acc = [(-9.81 * math.sin(angle[0]))/length]


i = 1
time = np.linspace(0,10,10000)
angNext = 0
velNext = 0
accNext = 0

def print_system(time,angle,velocity, acceleration):
    print("TIME:     ", time)
    print("ANGLE: ", angle)
    print("VELOCITY: ", velocity)
    print("ACCELERATION: ", acceleration, "\n")

def update_system(acc,angle,vel,time1,time2):
    dt = time2-time1
    angNext = angle+vel*dt
    velNext = vel+acc*dt
    accNext = (-9.81 * math.sin(angNext))/length
    #accNext = 9.8*(math.pi/2-angleNext)
    return angNext, velNext, accNext

while i < len(time)-1:
    #print(i)
    angNext, velNext, accNext = update_system(acc[i-1],angle[i-1], vel[i-1],time[i-1],time[i])
    acc.append(accNext)
    vel.append(velNext)
    angle.append(angNext)
    #print_system(time[i], angle[i],vel[i], acc[i])
    i = i + 1

plt.subplot(3,1,1)
plt.plot(time[:-1], angle, 'r--')

plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,2)
plt.plot(time[:-1], vel, 'r--')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()


plt.subplot(3,1,3)
plt.plot(time[:-1], acc, 'r--')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()
plt.tight_layout()