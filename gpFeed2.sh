#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./makePicAndSend.sh
./gpFeed.py D C
sleep 2m
./makePicAndSend.sh

