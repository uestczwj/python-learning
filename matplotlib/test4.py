from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd

df = pd.DataFrame([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])

data_list = df.values
length = len(df) - 1
index_lst = []

for j in range(len(df)):
    index_lst.append(j)
fig = plt.figure()

ax1 = fig.add_subplot(1, 1, 1, xlim=(0, length - 1), ylim=(0, 5000))
line, = ax1.plot([], [], lw=2)
xdata, ydata = [], []

def run(data):
  x,y = data
  xdata.append(x)
  ydata.append(y)
  line.set_data(xdata, ydata)
  return line,

def data_gen():
  cnt = 0
  while cnt < length:
    cnt+=1
    yield cnt, data_list[cnt]

# anim1 = animation.FuncAnimation(fig, animate, init_func=init, interval=2000)
ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=1, repeat=False)
plt.show()

print('Game over!')