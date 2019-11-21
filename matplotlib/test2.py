import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import  math
from matplotlib.pyplot import MultipleLocator

x_begin  = -10
x_end    = 13

y_begin  = 0
y_end    = x_end * 3

fig = plt.figure()
fig.set(alpha=0.3)
plt.axis([x_begin * 2, x_end * 2, y_begin, y_end])
plt.xlabel('x')
plt.ylabel('|x-3| + |x+2|')

plt.ion()

x_major_locator=MultipleLocator(1)
y_major_locator=MultipleLocator(1)

ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

x = []
y = []

for i in range(x_begin, x_end):
    x.append(i)
    y.append(abs(i-3) + abs(i-2))
    
    plt.plot(x, y)
    plt.pause(0.2)

plt.grid()
plt.show()

print('Game Over!')
