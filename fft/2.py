import  numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

COUNT = 256

# dual frequency signal
sampling_rate = 2**16
fft_size = 2**14
t = np.arange(0, 1, 1.0/sampling_rate)
x = np.array(map(lambda x : x*COUNT, t))
y = np.sqrt(2)*np.sin(2*np.pi*COUNT*t) + np.sqrt(2)*np.sqrt(2)*np.sin(2*np.pi*4*COUNT*t)
y = y + 0.005*np.random.normal(0.0,1.0,len(y))

plt.plot(y)
plt.grid()
plt.show()

