#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./makePicAndSend.sh
./gpFeed.py B A
sleep 2m
./makePicAndSend.sh
