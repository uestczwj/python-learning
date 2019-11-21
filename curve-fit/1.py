from dtw import *
import numpy as np
import matplotlib.pyplot as plt


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
    x = A * np.sin(2 * f0 * np.pi * n * T + phi)

    return x


def generate_sinusoid_2(t, A, f0, fs, phi):
    '''
    t  (float) : time length of the generated sequence
    A  (float) : amplitude
    f0 (float) : frequency
    fs (float) : sample rate
    phi(float) : initial phase

    returns
    x (numpy array): sinusoid signal sequence
    '''

    T = 1.0 / fs
    N = t / T

    return generate_sinusoid(N, A, f0, fs, phi)

A = 4
f0 = 10
fs = 500
phi = 0
t = 1

x = generate_sinusoid_2(t, A, f0, fs, phi)

n = np.arange(0, t, 1 / fs)
plt.plot(n, x)
plt.ylim(-A-1, A+1)
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.title('True signal in time domain')
plt.savefig('e_DFT1.eps', bbox_inches='tight')
plt.grid()
plt.show()

y1 = generate_sinusoid_2(t, 0.2*A, 2*f0, fs, 0)
y2 = generate_sinusoid_2(t, 0.1*A, 3*f0, fs, 0)
y3 = generate_sinusoid_2(t, 0.05*A, 4*f0, fs, 0)
y4 = generate_sinusoid_2(t, 0.025*A, 5*f0, fs, 0)


y = add_noise(x, 100, 20, 0.91)
y = add_noise(y,  200, 20, 1.15)
y = add_noise(y,  300, 20, 0.97)
y = add_noise(y,  400, 20, 1.02)
'''
A = 0.2
f1 = 100
fs = 500
phi = 0
t = 1

x1 = generate_sinusoid_2(t, A, f1, fs, phi)

n = np.arange(0, t, 1 / fs)
plt.plot(n, x1)
plt.ylim(-2.5, 2.5)
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.title('Noise signal in time domain')


plt.savefig('e_DFT2.eps', bbox_inches='tight')
plt.grid()
plt.show()

'''


#x = x + y1 + y2 + y3 + y4
n = np.arange(0, t, 1 / fs)
plt.plot(n, x)
plt.ylim(-A-1, A+1)
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.title('Input signal in time domain')

plt.savefig('e_DFT3.eps', bbox_inches='tight')
plt.grid()
plt.show()

from scipy.fftpack import fft

# fft is
X = fft(x + y)
mX = np.abs(X)  # magnitude
pX = np.angle(X)  # phase

for i in range(1, len(pX)+1):
    if i % f0 != 0:
        pX[i] = 0

plt.subplot(2,1,1)
plt.plot(mX / 250)
plt.xlabel('frequency(Hz)')
plt.ylabel('amplitude')
plt.title('Input signal in frequency domain')

plt.savefig('e_DFT4.eps', bbox_inches='tight')
plt.subplot(2,1,2)
plt.plot(pX)
plt.grid()
plt.show()



