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
      maxelementN int型   最新のデータから何個取得するか指定
      getdate             デフォルトは"today"だが別日の場合にはgetdate="20210730"のように指定する
      save_path   str型   読み込むファイルのパスを指定する
    
  '''
  #読み込むファイルが今日の場合
  if (getdate=="today"):
    now_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = save_path + now_str + ".csv"
  #読み込むファイルが別の日の場合
  else:
    now_str = getdate
    filename = save_path + now_str + ".csv"
  
  #ファイルを読み込む
  with open(filename, 'r') as csv_file:
    xdata = []
    ydata = []
    #読み込んだファイルを配列に代入する
    for row in csv.reader(csv_file, delimiter='\t'):
      xdata.append(row[0])#日付データ
      ydata.append(row[1])#数値データ
  
  #文字列データを変換する
  xdata_str = [datetime.datetime.strptime(data, '%Y/%m/%d %H:%M:%S') for data in xdata]
  ydata_str = [float(data) for data in ydata]

  #maxelementNより保存データ数が少ない場合には全てのデータを取得する
  rexdata_str = xdata_str[max(0,len(xdata_str)-maxelementN):]
  reydata_str = ydata_str[max(0,len(ydata_str)-maxelementN):]
  return [rexdata_str, reydata_str]
