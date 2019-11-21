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




plt.plot(x)
plt.grid()
plt.show()

plt.plot(y)
plt.grid()
plt.show()

# fft is
X = fft(y)
mX = np.abs(X)  # magnitude
pX = np.angle(X)  # phase

# plot the magnitude and phase
plt.subplot(2, 1, 1)
plt.plot(mX)

plt.subplot(2, 1, 2)
plt.plot(pX)
plt.show()

'''
## A noisy sine wave as query
idx = np.linspace(0,6.28,num=100)
query = np.sin(idx) + np.random.uniform(size=100)/10.0

## A cosine is for template; sin and cos are offset by 25 samples
template = np.cos(idx)

## Find the best match with the canonical recursion formula
alignment = dtw(query, template, keep_internals=True)
'''
alignment = dtw(x, y, keep_internals=True)
print(alignment.distance)


## And much more!

print("Game over!")
