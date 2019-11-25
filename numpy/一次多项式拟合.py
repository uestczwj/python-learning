import matplotlib.pyplot as plt
import numpy as np

x = [ 1 ,2  ,3 ,4 ,5 ,6]
y = [ 2.5 ,3.51 ,4.45 ,5.52 ,6.47 ,7.2]

z1 = np.polyfit(x, y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print(z1)  #[ 1.          1.49333333]
print(p1)  # 1 x + 1.493

print("y =  {} * x + {}".format(z1[0], z1[1]))

for i in range(len(x)):
    y_value = z1[0] * x[i] + z1[1]
    diff = y_value - y[i]
    print("diff = {}".format(diff))

plt.plot(x, y)
plt.show()

