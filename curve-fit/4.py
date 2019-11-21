import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def add_noise(y, start, len, diverse):
    for j in range(len):
        y[start + j] = y[start + j] * diverse

    return y

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


N = 1024
A = 1
f0 = 50
fs = 40000
phi = 0

x1 = generate_sinusoid(N, A,     f0,   fs, phi)
x2 = generate_sinusoid(N, A*0.1, f0*2, fs, phi)
x3 = generate_sinusoid(N, A*0.1, f0*3, fs, phi)
x4 = generate_sinusoid(N, A*0.1, f0*4, fs, phi)
x5 = generate_sinusoid(N, A*0.1, f0*5, fs, phi)

x = x1 + x2 + x3 + x4 + x5

x = add_noise(x, 5, 50, 0.91)
x = add_noise(x, 50, 50, 1.15)
x = add_noise(x, 100, 50, 0.97)
x = add_noise(x, 150, 60, 1.22)

plt.plot(x)
plt.show()

# fft is
X = fft(x)
mX = np.abs(X)  # magnitude
pX = np.angle(X)  # phase

# plot the magnitude and phase
plt.subplot(2, 1, 1)
plt.plot(mX)

plt.subplot(2, 1, 2)
plt.plot(pX)
plt.show()

print("Game over!")
