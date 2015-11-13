#! /usr/bin/env python 
import numpy
import nupic
import math
import csv
import datetime, time

#  Read the FDX stock price and correlate it against the unemployment rate.  
#  correlate the FDX stock price against the adjusted trade volume with China
#  against short term interest rate.  
#  




def readFdx():
  filename="../fdx.csv"
  print filename
  fileHandleReader = open( filename) 
  csvReader = csv.reader(fileHandleReader)
  csvReader.next()
  csvReader.next()
  csvReader.next()
  myList = list
  for row in csvReader:
    theDay = repr(datetime.datetime(*time.strptime(row[0], "%Y-%m-%d")[:6])) 
    myList.append( theDay)
    
  for l in list:
    print l
    
if __name__ == "__main__":
  readFdx()

