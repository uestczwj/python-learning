import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from dtw import *
import pandas as pd

plt.cla()
plt.clf()

FILE_COUNT    = 101
POINT_COUNT   = 1024


data         = [[0] * POINT_COUNT]* 6
b_current    = [[0] * POINT_COUNT]* FILE_COUNT
diff         = [[0] * POINT_COUNT]* FILE_COUNT
avg_diff     = [0] * POINT_COUNT

for i in range(0, FILE_COUNT):
    data = pd.read_table("./data/vc_{}.txt".format(i), header=None)
    b_current[i] = np.array(data[5])

M = np.max(b_current)
A = 5
factor = M / A

for i in range(0, FILE_COUNT):
    b_current[i] = b_current[i] / factor

SECTION_LEN    = 32

fit_current = [[0] * POINT_COUNT] * FILE_COUNT

for section_len in [4, 8, 16, 32, 64]:
    SECTION_LEN = section_len
    sum_of_disance = 0
    section_count = POINT_COUNT // SECTION_LEN
    start = time.time()

    for i in range(0, FILE_COUNT):
        for j in range(section_count):
            x1 = np.linspace(0, SECTION_LEN-1, num=SECTION_LEN)
            x1 = np.asarray(x1).reshape(-1, 1)
            y = b_current[i][SECTION_LEN * j : SECTION_LEN*(j+1)]
            y = np.asarray(y).reshape(-1, 1)

            reg = LinearRegression().fit(x1, y)
            #print("一元回归方程为:  Y = %.5fX + (%.5f)" % (reg.coef_[0], reg.intercept_[0]))

            for p in range(len(x1)):
                value = x1[p] * reg.coef_[0] + reg.intercept_[0]
                #print("y[{}] = {}, fit[{}] = {}".format(p+SECTION_LEN * j, y[p], p+SECTION_LEN * j, value))
                fit_current[i][p+SECTION_LEN * j] = value

        dis0 = dtw(b_current[i], fit_current[i], keep_internals=True).distance
        sum_of_disance = sum_of_disance + dis0
        '''
        print("fit_current : distance_{} = {}".format(i, dis0))

        plt.title("fit_current[{}]".format(i))
        plt.subplot(211)
        plt.plot(fit_current[i])
        plt.grid()
    
        plt.title("b_current[{}]".format(i))
        plt.subplot(212)
        plt.plot(b_current[i])
        plt.grid()
        plt.show()
        '''
    end = time.time()
    print("SECTION_LEN = {}, avg_distance = {}, Use time = {}秒.".format(SECTION_LEN, sum_of_disance / FILE_COUNT, str(end-start)))