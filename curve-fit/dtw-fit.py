import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from dtw import *
import pandas as pd

plt.cla()
plt.clf()

def generate_sinusoid(N, A, f0, fs, phi):
    '''
    N(int) : number of samples
    A(float) : amplitude
    f0(float): frequency in Hz
    fs(float): sample rate
    phi(float): initial phase

    return
    x (numpy array): sinusoid signal which lenght is M
    '''

    T = 1 / fs
    n = np.arange(N)  # [0,1,..., N-1]
    x = A * np.cos(2 * f0 * np.pi * n * T + phi)
    return x

FILE_COUNT    = 101
POINT_COUNT   = 1024


data         = [[0] * POINT_COUNT]* 6
b_current    = [[0] * POINT_COUNT]* FILE_COUNT
diff         = [[0] * POINT_COUNT]* FILE_COUNT
avg_diff     = [0] * POINT_COUNT

for i in range(0, FILE_COUNT):
    data = pd.read_table("./data/vc_{}.txt".format(i), header=None)
    b_current[i] = np.array(data[5])

'''    
    plt.plot(b_current[i])
    plt.grid()
    plt.title("B current")
    plt.show()
'''

M = np.max(b_current)

N = 1024
f0 = 10
fs = 5000
best_phi = 0

dis0 = 999999999999999
START_PAHSE = 347
bCurrent = b_current[(int)(FILE_COUNT / 2)]
for phase in range(START_PAHSE, 360):
    x = generate_sinusoid(N, M, f0, fs, phase)
    dis1 = dtw(x, bCurrent, keep_internals=True).distance

    if dis1 < dis0:
        print("phase = {}, distance = {} ".format(phase, dis1))

        dis0 = dis1
        best_phi = phase

        plt.subplot(211)
        plt.plot(bCurrent)
        plt.grid()
        plt.title("Phase  = {}".format(phase))

        plt.subplot(212)
        plt.plot(x)
        plt.grid()
        plt.title("Gen sine wave")
        plt.show()
    #time.sleep(2)

print("correct phase : ", best_phi)

N = 1024
A = 5
f0 = 10
fs = 5000
#phi = 45

x = generate_sinusoid(N, A, f0, fs, best_phi)
factor = M / A

for i in range(0, FILE_COUNT):
    b_current[i] = b_current[i] / factor
    diff[i] = b_current[i] - x
    avg_diff = avg_diff + diff[i]

avg_diff = avg_diff / FILE_COUNT

dis0 = 0
dis1 = 1
current = [0] * POINT_COUNT
for i in range(0, FILE_COUNT):
    dis0 = dtw(x, b_current[i], keep_internals=True).distance

    current = b_current[i] - avg_diff
    dis1 = dtw(x, current, keep_internals=True).distance

    print("data_{}, distance from {} --> {}".format(i, dis0, dis1))

    plt.title("vc_{}.txt".format(i))
    plt.subplot(211)
    plt.plot(current)
    plt.grid()

    plt.subplot(212)
    plt.plot(x)
    plt.grid()
    plt.show()


SECTION_LEN    = 16
section_count  = POINT_COUNT // SECTION_LEN

fit_current = [[0] * POINT_COUNT] * FILE_COUNT

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