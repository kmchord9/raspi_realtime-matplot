# -*- coding:utf-8 -*-

import csv
import datetime

def saveCSV(time, data, save_path="./datalog/"):
  now_str = datetime.datetime.now().strftime("%Y%m%d")
  filename = save_path + now_str + ".csv"
  with open(filename, 'a') as f:
    strTime = time.strftime("%Y/%m/%d %H:%M:%S")
    addStr = strTime + "\t" + str(data)
    
    print(addStr, file=f)

def loadTodayCSV(maxelementN, getdate="today"):
  save_path = "./datalog/"
  if not (getdate=="today"):
    now_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = save_path + now_str + ".csv"
  else:
    now_str = getdate
    filename = save_path + now_str + ".csv"

  csv_file = open(filename, 'r')

  xdata = []
  ydata = []
  reVal = []

  for row in csv.reader(csv_file, delimiter='\t'):
    xdata.append(row[0])
    ydata.append(row[1])
        
  if xdata < maxelementN: 
    reVal.append([datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S') for data in xdata])
    reVal.append([float(data) for data in ydata])
  else:
    reVal.append([datetime.datetime.strptime(data, '%y/%m/%d %h:%m:%s') for data in xdata][:maxelementN])
    reVal.append([float(data) for data in ydata][:maxelementN])

  return reVal
