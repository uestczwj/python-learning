import time
import matplotlib.pyplot as plt
import numpy as np
import  math

x_begin  = -10
x_end    = 13

y_begin  = 0
y_end    = x_end * 3

fig = plt.figure()
fig.set(alpha=0.3)
plt.ion()

plt.axis([x_begin * 2, x_end * 2, y_begin, y_end])
plt.xlabel('x')
plt.ylabel('|x-3| + |x+2|')


x = []
y = []

for i in range(x_begin, x_end):
    x.append(i)
    y.append(abs(x-3) + abs(x-2))
    
    plt.plot(x, y)
    plt.pause(0.2)

print('Game Over!')
