#!/usr/bin/python

import sys, imaplib, email


if len(sys.argv) != 1:
    print "No Argument needed"
    sys.exit(0)

#print filenameData
def readFromMailAdrAndPwAndToMailAdr():
  f=open("mail.txt", "r")
  content = f.readlines()
  content = [x.strip('\n') for x in content]
  return content[0], content[1], content[2]

def readUnreadMail(mailAdr, pw, fromAdr):
  mail = imaplib.IMAP4_SSL('imap.gmail.com')
  (retcode, capabilities) = mail.login(mailAdr, pw)
  mail.list()
  mail.select('inbox')

  n=0
  subs=[]
  #(retcode, messages) = mail.search(None, '(UNSEEN)')
  filterStr = '(FROM ' + fromAdr + ' UNSEEN)'
  (retcode, messages) = mail.search(None, filterStr)
  if retcode == 'OK':

   for num in messages[0].split() :
    n=n+1
    typ, data = mail.fetch(num,'(RFC822)')
    for response_part in data:
      if isinstance(response_part, tuple):
        original = email.message_from_string(response_part[1])
        #print original['From']
        subs.append(original['Subject'])
        # mark mail as read
        typ, data = mail.store(num,'+FLAGS','\\Seen')
  return subs

fromAdr, pw, toAdr = readFromMailAdrAndPwAndToMailAdr()
subs = readUnreadMail(fromAdr, pw, toAdr)
# to string
val = " "
print val.join(subs)
