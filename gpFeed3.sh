#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./makePicAndSend.sh
./gpFeed.py F E
sleep 2m
./makePicAndSend.sh

