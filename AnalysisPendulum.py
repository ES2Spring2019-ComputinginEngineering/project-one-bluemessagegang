#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:59:36 2019

@author: Bowton Eaves / Grace Anderson


        Parsing of Real-World Data
"""


import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

#Change name of file here vvv to use different data

#Files in order of longest to shortest length
#869
#587
#19
#231
#875


fin = open("pendulumData 869.txt")

list_lines = []
accX = []
accY = []
accZ = []
time = []
angle = []

#Reading of the file to produce the deta

for line in fin:
    accX.append(int(line.split(",")[0]))
    accY.append(int(line.split(",")[1]))
    accZ.append(int(line.split(",")[2]))
    time.append(float(line.split(",")[3].strip()))
    angle.append(math.atan2(-1*int(line.split(",")[1]),int(line.split(",")[2])))

time = np.array(time)
filtAngle = sig.medfilt(angle,9)
peaks,_ = sig.find_peaks(filtAngle)


#Calculation of Period

i=0
firstPeriod = time[peaks[i+1]]-time[peaks[0]]
while i<4:
    nextPeriod = time[peaks[i+2]]-time[peaks[i+1]]
    avgP = (firstPeriod+nextPeriod)/2
    firstPeriod = nextPeriod
    i = i + 1
    
print("Period of pendulum = ")
print(avgP)

#Graph of Unfiltered Angle vs. Time
plt.figure()
plt.plot(time, angle, 'k-')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (Theta)')
plt.title('Theta vs Time')
plt.show()

#Graph of Filtered Angle vs. Time
plt.figure()
plt.plot(time, filtAngle, 'k-', time[peaks], filtAngle[peaks], 'b.')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle (Theta)')
plt.title('Filtered - Theta vs Time')
plt.show()

#Graph of Acceleration
plt.figure()
plt.plot(time, accY, 'r-') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
#plt.xlim((0, 10)) # set x range to -1 to 8
plt.grid()
plt.show()

