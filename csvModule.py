# -*- coding:utf-8 -*-

import csv
import datetime

def saveCSV(time, data, save_path="./datalog/"):
  '''
    今日の日付でcsvファイルを作成して時間とデータを書き込む
    引数：
      time        datetime型
      data        float型
      save_path   str型
    save_pathで保存するディレクトリを指定する。
  '''
  #今日の日付を取得
  now_str = datetime.datetime.now().strftime("%Y%m%d")
  #CSVファイル保存場所のパスを生成
  filename = save_path + now_str + ".csv"

  #csvファイルを開いてデータを書き込み
  with open(filename, 'a') as f:
    strTime = time.strftime("%Y/%m/%d %H:%M:%S")
    addStr = strTime + "\t" + str(data)
    
    print(addStr, file=f)

def loadTodayCSV(maxelementN, getdate="today", save_path="./datalog/"):
  '''
    今日の日付でcsvファイルを作成して時間とデータを書き込む
    引数：
      time        datetime型
      data        float型
      save_path   str型
    save_pathで保存するディレクトリを指定する。
  '''
  #save_path = "./datalog/"
  if (getdate=="today"):
    now_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = save_path + now_str + ".csv"
  else:
    now_str = getdate
    filename = save_path + now_str + ".csv"

  #csv_file = open(filename, 'r')

  with open(filename, 'r') as csv_file:
    xdata = []
    ydata = []

    for row in csv.reader(csv_file, delimiter='\t'):
      xdata.append(row[0])
      ydata.append(row[1])

  xdata_str = [datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S') for data in xdata]
  ydata_str = [float(data) for data in ydata]

  #if len(xdata) < maxelementN:
  #    return [xdata_str, ydata_str]

  #else:
  rexdata_str = xdata_str[max(0,len(xdata_str)-maxelementN):]
  reydata_str = ydata_str[max(0,len(ydata_str)-maxelementN):]
  return [rexdata_str, reydata_str]
