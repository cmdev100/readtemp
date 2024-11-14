#!/usr/bin/python
#-----------------------------------------
#
#	GetMomentanValue.py
#   Get a momentan value from the DS18B20 sensor
#
# Athor : Christian Meijer
# Date  : 2016-12-19
#
#-----------------------------------------

import GetValue

if __name__ == '__main__':

  tValue = GetValue.gettemp()

  print ('{:.2f}'.format(tValue))
