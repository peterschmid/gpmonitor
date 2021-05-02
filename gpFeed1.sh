#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./makePicAndSend.sh
./gpFeed.py B A
./makePicAndSend.sh
