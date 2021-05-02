#!/bin/bash

DATE=$(date +'%Y_%m_%d')
DATETIME=$(date +'%Y%m%d_%H_%M_%S')
FILENAME="gp_$DATETIME.jpg"

#make pic
raspistill -o "$FILENAME" --timeout 500


# send mail
./sendPic.py $FILENAME

