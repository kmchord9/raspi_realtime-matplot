# -*- conding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import datetime
import random
#from adt7410_13bit import getTemp
from csvModule import saveCSV, loadTodayCSV

SAVE_CYCLE_TIME = 1
SAVE_PATH = "./datalog/"
MAX_SHOW_ELEMENT_N = 540

def randomTemp():
    return np.round(random.random()*20,2)

def pause_plot():
    fig, ax = plt.subplots(1,1)

    todayData = []
    try:

        todayData = loadTodayCSV(MAX_SHOW_ELEMENT_N)
        xVal = np.array(todayData[0])
        yVal = np.array(todayData[1])
        lines, = ax.plot(xVal,yVal)

    except FileNotFoundError as e:
        dt_now = datetime.datetime.now()
        xVal = np.array([ dt_now ])
        yVal = np.array([randomTemp()])
        lines, = ax.plot(xVal,yVal)

    except Exception as e:
        print(e)

    while True:

        #今の時間と温度を取得
        dt_now = datetime.datetime.now()
        tm_now = randomTemp()

        #csvに保存
        saveCSV(dt_now, tm_now)

        #設定した数より多い場合には先頭を消して末尾に追加
        if xVal.size > MAX_SHOW_ELEMENT_N:
            xVal = np.roll(xVal, -1)
            yVal = np.roll(yVal, -1)

            xVal[-1] = dt_now
            yVal[-1] = tm_now

        else:

            xVal = np.append(xVal, dt_now)
            yVal = np.append(yVal, tm_now)

        lines.set_data(xVal,yVal)
        ax.set_xlim((xVal.min(), xVal.max()))
        ax.set_ylim((yVal.min(), yVal.max()))
        plt.pause(SAVE_CYCLE_TIME)


if __name__=="__main__":
    pause_plot()
