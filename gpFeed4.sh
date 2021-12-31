#!/bin/bash
stty -F /dev/ttyACM0 -hupcl
./makePicAndSend.sh
./gpFeed.py H G
sleep 2m
./makePicAndSend.sh

