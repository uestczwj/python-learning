import pandas as pd #数据分析
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from dtw import *
import time
import os
import pandas
import codecs
import glob
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

FILE_COUNT    = 102
POINT_COUNT   = 1024


data         = [[0] * POINT_COUNT]* 6
b_current    = [[0] * POINT_COUNT]* FILE_COUNT
diff         = [[0] * POINT_COUNT]* FILE_COUNT
avg_diff     = [0] * POINT_COUNT

for i in range(0, FILE_COUNT):
    data = pd.read_table("./data/vc_{}.txt".format(i), header=None)
    b_current[i] = data[5]

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
phi = 0

dis0 = 999999999999999
#phi = 148    #for "data0.csv"

bCurrent = b_current[(int)(FILE_COUNT / 2)]
for p in range(0, 360):
    x = generate_sinusoid(N, M, f0, fs, p)
    dis1 = dtw(x, bCurrent, keep_internals=True).distance

    if dis1 < dis0:
        print("phase = {}, distance = {} ".format(p, dis1))

        dis0 = dis1
        phi = p

        plt.subplot(211)
        plt.plot(b_current[i])
        plt.grid()
        plt.title("Phase B current")

        plt.subplot(212)
        plt.plot(x)
        plt.grid()
        plt.title("Gen sine wave")
        plt.show()
    #time.sleep(2)

print("correct phase : ", phi)

N = 1024
A = 5
f0 = 10
fs = 5000
#phi = 45

x = generate_sinusoid(N, A, f0, fs, phi)
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