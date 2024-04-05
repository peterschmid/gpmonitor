#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./gpFeed.py Z Y

