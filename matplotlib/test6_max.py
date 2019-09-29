import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

x_begin     = -10
zero_points = [3, -2]

abs_count = len(zero_points)
x_end    = abs(x_begin)

x_major_locator=MultipleLocator(1)
y_major_locator=MultipleLocator(1)

ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.axis([x_begin, x_end, -x_end * abs_count, x_end * abs_count])

plt.ion()

xs = [x_begin, x_begin]
ys = [x_end * abs_count, x_end * abs_count]
y = 0

for i in range(x_begin, x_end+1):
    y = abs(i - zero_points[0]) -  abs(i - zero_points[1])
        
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys)
    plt.pause(0.1)

plt.ioff()
plt.grid()
plt.show()

print('game over')
