#!/bin/bash
val=$(/home/pi/readMail.py)
#val=$(./test.py)

#echo "$val"

for word in $val
do
  OPTION=$word
  case $OPTION in
  Pic1)
  echo "Take Picture 1"
  /home/pi/makePicAndSend.sh
  ;;

  Feed1)
  echo "Feed Station 1"
  /home/pi/gpFeed1.sh
  ;;

  Feed2)
  echo "Feed Station 2"
  /home/pi/gpFeed2.sh
  ;;

  Feed3)
  echo "Feed Station 3"
  /home/pi/gpFeed3.sh
  ;;

  Feed4)
  echo "Feed Station 4"
  /home/pi/gpFeed4.sh
  ;;

  Help)
  echo "Send Help Text"
  /home/pi/sendHelp.py
  ;;

  help)
  echo "Send Help Text"
  /home/pi/sendHelp.py
  ;;

  *)
  echo “No Action”
esac

done
