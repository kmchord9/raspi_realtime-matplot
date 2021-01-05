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
  if (getdate=="today"):
    now_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = save_path + now_str + ".csv"
  else:
    now_str = getdate
    filename = save_path + now_str + ".csv"

  csv_file = open(filename, 'r')

  xdata = []
  ydata = []

  for row in csv.reader(csv_file, delimiter='\t'):
    xdata.append(row[0])
    ydata.append(row[1])

  xdata_str = [datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S') for data in xdata]
  ydata_str = [float(data) for data in ydata]

  if len(xdata) < maxelementN:
      return [xdata_str, ydata_str]

  else:
      rexdata_str = xdata_str[max(0,len(xdata_str)-maxelementN):]
      reydata_str = ydata_str[max(0,len(ydata_str)-maxelementN):]
      return [rexdata_str, reydata_str]
