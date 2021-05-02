#!/usr/bin/python

import serial  # Importing the serial library to communicate with Arduino
import time
import sys

if len(sys.argv) != 3:
  print "2 Parameter neede: Up char and down char"
  exit(1)

ser = serial.Serial('/dev/ttyACM0', 9600)
print ser.name
print "Send " + sys.argv[1] + " to arduino"
ser.write(sys.argv[1])
time.sleep(1)
print "Send " + sys.argv[2] + " to arduino"
ser.write(sys.argv[2])
ser.close()
