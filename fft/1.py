import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


def generate_real_signal(num_sample, A, k0):
    '''
    generate real signal

    num_sample : 信号的个数，即公式中的N
    A  : 振幅
    k0 : 周期个数

    returns
    x : 实数信号
    '''
    hN = num_sample // 2
    n = np.arange(-hN, hN)
    x = A * np.cos(2 * np.pi * k0 * n / num_sample)

    return x

# DFT and plot the results
num_sample = 100
k0 = 20
A = 0.8

x = generate_real_signal(num_sample, A, k0)
x1 = generate_real_signal(num_sample, 0.01*A, 2*k0)
x2 = generate_real_signal(num_sample, 0.01*A, 3*k0)
x3 = generate_real_signal(num_sample, 0.01*A, 4*k0)
x4 = generate_real_signal(num_sample, 0.01*A, 5*k0)

#x = x + x1 + x2 + x3 + x4

X = fft(x)

plt.figure(figsize=(10,6))
plt.subplot(311)
plt.plot(x)

plt.subplot(312)
plt.plot(np.real(X))

hM1 = (num_sample+1)//2
hM2 = num_sample//2
Y = np.zeros(num_sample)
Y[:hM1] = X[-hM1:]
Y[-hM2:] = X[:hM1]
plt.subplot(313)
x_axis = np.arange(-hM1, hM2)
plt.plot(x_axis, np.real(Y))
plt.show()