#!/bin/bash
val=$(/home/pi/readMail.py)
#val=$(./test.py)

#echo "$val"

for word in $val
do
  OPTION=$word
  case $OPTION in
  pic1)
  #echo "Take Picture 1"
  /home/pi/makePicAndSend.sh
  ;;

  pic2)
  echo "Take Picture 2"
  ;;

  *)
  echo “No Action”
esac

done
