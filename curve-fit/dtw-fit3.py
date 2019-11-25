import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from dtw import *
import pandas as pd

FILE_COUNT    = 101
POINT_COUNT   = 1024

def polyfit(x, y, degree):
    results = {}
    coeffs = numpy.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot #准确率
    return results


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
section_count  = POINT_COUNT // SECTION_LEN

fit_current = [[0] * POINT_COUNT] * FILE_COUNT

for i in range(0, FILE_COUNT):
    for j in range(section_count):
        x1 = np.linspace(0, SECTION_LEN-1, num=SECTION_LEN)
        #x1 = np.asarray(x1).reshape(-1, 1)
        y = b_current[i][SECTION_LEN * j : SECTION_LEN*(j+1)]
        #y = np.asarray(y).reshape(-1, 1)

        z1 = polyfit(x1, y, 2)

        for p in range(len(x1)):
            value = z1['polynomial'][0] * x1[p] * x1[p] + z1['polynomial'][1] * x1[p] + z1['polynomial'][0]
            #print("y[{}] = {}, fit[{}] = {}".format(p+SECTION_LEN * j, y[p], p+SECTION_LEN * j, value))
            fit_current[i][p+SECTION_LEN * j] = value

    dis0 = dtw(b_current[i], fit_current[i], keep_internals=True).distance
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