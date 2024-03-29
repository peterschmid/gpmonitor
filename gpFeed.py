#!/usr/bin/python

import serial  # Importing the serial library to communicate with Arduino
import time
import sys

if len(sys.argv) != 3:
  print ("2 Parameter neede: Up char and down char")
  exit(1)

ser = serial.Serial(
        port='/dev/ttyACM0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

print (ser.name)
print ("Send " + sys.argv[1] + " to arduino")
#ser.write(sys.argv[1])
ser.write(sys.argv[1].encode())
time.sleep(1)
print ("Send " + sys.argv[2] + " to arduino")
#ser.write(sys.argv[2])
ser.write(sys.argv[2].encode())
ser.close()
