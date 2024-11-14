#!/usr/bin/python
#--------------------------------------
#
#              GetValue.py
#  Read DS18B20 1-wire temperature sensor
#
# Author : Christian Meijer
# Date   : 2016-12-17
#
#
#--------------------------------------

def gettemp():
  try:
   
    id = '28-80000026bb60'

    mytemp = ''
   
    filename = 'w1_slave'
   
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
   
    line = f.readline() # read 1st line

    crc = line.rsplit(' ',1)

    crc = crc[1].replace('\n', '')

    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999

    f.close()

    return int(mytemp[1])/float(1000)

  except:
    return 99999
