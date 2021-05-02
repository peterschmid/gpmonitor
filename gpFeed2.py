#!/usr/bin/python

import serial  # Importing the serial library to communicate with Arduino
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
print ser.name
print "Send D to arduino"
ser.write(b'D')
time.sleep(1)
print "Send C to arduino"
ser.write(b'C')
ser.close()
