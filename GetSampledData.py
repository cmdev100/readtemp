#!/usr/bin/python

import sqlite3
import sys
import time
import string
from datetime import datetime, timedelta


def getStoredValues(dbName, valueCount):
  
  qSql = "SELECT * FROM Temp ORDER BY Timestamp DESC"
  
  if valueCount != 0:
    qSql = qSql + " LIMIT {}".format(valueCount)  
  
  try:
    con = sqlite3.connect(dbName)
    
    cur = con.cursor()    
    cur.execute(qSql)

    aList = []
    
    for row in cur:      
      item = (row[0], row[1], row[2])      
      aList.append(item)   

    aList.sort(key=lambda t: t[1])
    
    return aList
         
  except sqlite3.Error as e:
    print ("Error %s:" % e.args[0])
    sys.exit(1)

  finally:
    if con:
     con.close()

