# -*- conding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import datetime
from adt7410_13bit import getTemp
from csvModule import saveCSV

SAVE_CYCLE_TIME = 1
SAVE_PATH = "./datalog/"
MAX_SHOW_ELEMENT_N = 540

def pause_plot():
    fig, ax = plt.subplots(1,1)

    dt_now = datetime.datetime.now()
    xVal = np.array([ dt_now ])
    yVal = np.array([getTemp()])
    lines, = ax.plot(xVal,yVal)

    while True:

        dt_now = datetime.datetime.now()
        tm_now = getTemp()

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
        plt.pause(SAVE_CYCLE_TIME)


if __name__=="__main__":
    pause_plot()

