#!/usr/bin/python

import serial  # Importing the serial library to communicate with Arduino
import time

#ser = serial.Serial('/dev/ttyACM0', 9600)
#ser = serial.Serial('/dev/ttyAMA0', 9600)
ser = serial.Serial(
        port='/dev/ttyACM0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
print (ser.name)
print ("Send B to arduino")
ser.write(b'B')
time.sleep(1)
print ("Send A to arduino")
ser.write(b'A')
ser.close()
