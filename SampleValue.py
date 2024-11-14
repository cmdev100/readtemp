#!/usr/bin/python
#--------------------------------------
#
#              SampleValue.py
#  Read DS18B20 1-wire temperature sensor
#  and store values into a sqlite database
#
# Author : Christian Meijer
# Date   : 2016-12-17
#
#--------------------------------------

import GetValue
import sqlite3
import sys
import time
import os.path
from datetime import datetime

def createDB(dbName):
  
  con = None

  try:
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    cur.execute('CREATE TABLE temp (Id INTEGER NOT NULL, Timestamp INTEGER NOT NULL, Value REAL NOT NULL, CONSTRAINT PK_Temp PRIMARY KEY(Id, Timestamp))')

  except sqlite3.Error as e:
    
    print ("Error %s:" % e.args[0])
    sys.exit(1)
    
  finally:
    if con:
      con.close()  

def storeTemp(dbName,timeStamp,tempValue):

  if not os.path.exists(dbName):
    createDB(dbName)
  
  
  param = [1, int(time.mktime(timeStamp.timetuple())), tempValue]

  try:
    con = sqlite3.connect(dbName)
 
    cur = con.cursor()
    cur.execute("INSERT INTO temp VALUES (?, ?, ?)", param)	

    con.commit()
  except sqlite3.Error as e:
    print ("Error %s:" % e.args[0])
    sys.exit(1)	

  finally:
    if con:
      con.close()
