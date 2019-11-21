import pandas as pd #数据分析
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from dtw import *

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



data = pd.read_csv("data.csv")
b_current = data.b_current

m = np.max(b_current)

b_current = b_current / m

plt.plot(b_current)
plt.title('b_current')
plt.grid()
plt.show()
print(b_current)

N = 1024
A = m
f0 = 10
fs = 5000
phi = 0

x = generate_sinusoid(N, A, f0, fs, phi)

x = x / m

alignment = dtw(x, b_current, keep_internals=True)
print("DTW distance  of x and b_current : ")
print(alignment.distance)


plt.subplot(2,1,1)
plt.plot(b_current)
plt.grid()

plt.subplot(2,1,2)
plt.plot(x)

plt.grid()
plt.show()




