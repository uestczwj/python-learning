import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

zero_points = [-6, -2, 2, 6]
pause_time  = 0.2

zero_abs    = [abs(x) for x in zero_points]
x_begin     = (max(zero_abs) + 2) * (-1)
axis_factor = 1.1
zeros_count = len(zero_points)
x_end       = abs(x_begin)
x_axis      = x_end * axis_factor

x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(1)

ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.ion()

plt.axis([-x_axis, x_axis, 0, x_axis * zeros_count])

x = []
y = []

y_min = sum(zero_abs)
y_max = 0

def get_y(i, zeros_count):
    val = 0
    for j in range(zeros_count):
        val = val + abs(i - zero_points[j])

    return  val

def get_y_label(zeros_count):
    y_label = ""

    for i in range(zeros_count):
        if zero_points[i] > 0:
            y_label = y_label + '|x - ' + str(zero_points[i]) + '|'
        elif zero_points[i] == 0:
            y_label = y_label + '|x|'
        else:
            y_label = y_label + '|x + ' + str(abs(zero_points[i])) + '|'

        if i < zeros_count - 1:
            y_label = y_label + ' + '

    return y_label

for i in range(x_begin, x_end+1):
    x.append(i)
    y_val = get_y(i, zeros_count)

    y_min = min(y_min, y_val)
    y_max = max(y_max, y_val)

    y.append(y_val)

    plt.plot(x, y, 'go')
    plt.pause(pause_time)

plt.ioff()
plt.xlabel('x')
plt.ylabel(get_y_label(zeros_count))
plt.axis([-x_axis, x_axis, y_min - 1, y_max + 1])
plt.grid()
plt.show()

print('game over')
