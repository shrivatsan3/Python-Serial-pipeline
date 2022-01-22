# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:42:51 2022

@author: shriv
"""

#pip install pyserial 

# Importing libraries
import serial
import time

import numpy as np
# import numpy with the namespace np

import matplotlib.animation as animation
import matplotlib.pyplot as plt


arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
# Create a serial object by calling the constructor of class serial.Serial


_sineData = np.array([]) # from the namespace np, import the data type array
#_timeStamp = np.array([])
plt.show()

#startTime  = time.time()
#def animate(i):
while True:    
    _arduinoRead = arduino.readline() # read one byte of data from the serial port
    _arduinoRead = _arduinoRead.decode('ASCII') #decode the incoming data 
    try:
        _arduinoRead = float(_arduinoRead) #type cast to float
    except ValueError:
        continue
   
    #print(type(_arduinoRead))
   #print(_arduinoRead)
    _sineData = np.append(_sineData,_arduinoRead) 
    # add new data to old array and create a new array
    _avg = np.mean(_sineData) #from the namespace np, use method called mean
    #print(len(_sineData))
   #np.append(_timeStamp,time.time()-startTime)
    #np.append(_timeStamp,i)
    #print(len(_sineData))
    
    #from the namespace plt, import the following methods
    #syntax -> plt.method_name()
    plt.cla()
    plt.plot(_sineData)
    plt.xlabel("Amplitude")
    plt.ylabel=("index")
    plt.title("Sine wave %f"%_avg)
    plt.autoscale()
    plt.pause(0.05)

#ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
#plt.show()
