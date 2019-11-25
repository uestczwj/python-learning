import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from dtw import *
import pandas as pd
import time

FILE_COUNT    = 101
POINT_COUNT   = 1024

print("Use numpy.polyfit : curve count = {}".format(FILE_COUNT))

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

SECTION_LEN    = 16
fit_current = [[0] * POINT_COUNT] * FILE_COUNT

def run_fit(section_len):
    section_count = POINT_COUNT // section_len
    start = time.time()
    sum_of_disance = 0
    for i in range(0, FILE_COUNT):
        for j in range(section_count):
            x1 = np.linspace(0, section_len-1, num=section_len)
            y = b_current[i][section_len * j : section_len*(j+1)]

            z1 = np.polyfit(x1, y, 1)  # 一次多项式拟合，相当于线性拟合
            #print("一元回归方程为:  Y = %.5fX + (%.5f)" % (reg.coef_[0], reg.intercept_[0]))

            for p in range(len(x1)):
                value = z1[0] * x1[p] + z1[1]
                #print("y[{}] = {}, fit[{}] = {}".format(p+section_len * j, y[p], p+section_len * j, value))
                fit_current[i][p+section_len * j] = value

        dis0 = dtw(b_current[i], fit_current[i], keep_internals=True).distance
        sum_of_disance = sum_of_disance + dis0
        #print("fit_current : distance_{} = {}".format(i, dis0))
        '''
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
    print("SECTION_LEN = {}, avg_distance = {}, Use time = {}秒.".format(section_len, sum_of_disance / FILE_COUNT, str(end-start)))

for l in [4, 8, 16, 32, 64]:
    run_fit(l)