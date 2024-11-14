#!/usr/bin/python

import GetSampledData
import sys
import time

if len(sys.argv) > 1:
  param = sys.argv[1]
  try:
    valueCount = int(param)
  except:
    valueCount = 24
else:
  valueCount = 24

res = GetSampledData.getStoredValues('./data.db', valueCount)

for row in res:
  print ('({} | {} | {:.2f})'.format(row[0],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row[1])), row[2]))


