#!/usr/bin/python
#----------------------------------------
#
#	    Terminal.py 
#    Samples a temp value every hour   
# 
# Author  :  Christian Meijer
# Date    :  2016-12-19
#
#----------------------------------------

from datetime import datetime
import SampleValue
import GetValue
import time

dbName = 'data.db'

sampleDone = False;

while True:
  time.sleep(5)
  dt = datetime.now().replace(second=0, microsecond=0)

  if dt.minute == 0:
    if not sampleDone:
      tempValue = GetValue.gettemp()
      SampleValue.storeTemp(dbName, dt, tempValue)
      sampleDone = True
  else:
    sampleDone = False
