#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./makePicAndSend.sh
./gpFeed.py D C
./makePicAndSend.sh

