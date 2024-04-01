#!/usr/bin/python

import sys
from sendMail import sendSingleTextMail


if len(sys.argv) != 1:
    print ("No Arguments needed")
    sys.exit(0)

sendSingleTextMail("Help Text", "Pic1 = Send Picture, Feed1 to Feed4 = Drop food portion 1 to 4")
