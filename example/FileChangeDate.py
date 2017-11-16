# !/usr/bin/python

import os, sys

# Showing stat information of file
stinfo = os.stat('C:\\Users\\Anass.Ben\\Downloads\\umsaetze-5443833-2017-08-24-22-31-25.csv')
print (stinfo)

# Using os.stat to recieve atime and mtime of file
print ("access time of a2.py: %s" %stinfo.st_atime)
print ("modified time of a2.py: %s" %stinfo.st_mtime)

# Modifying atime and mtime
os.utime('C:\\Users\\Anass.Ben\\Downloads\\umsaetze-5443833-2017-08-24-22-31-25.csv',(1503610651.978733, 1503610651.978833))
print ("done!!")
