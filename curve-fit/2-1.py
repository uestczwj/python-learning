#-*- coding: utf-8 -*-
# python 3.5.0

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.asarray(np.linspace(1, 50)).reshape(-1, 1)
y = np.asarray(np.linspace(1, 50)).reshape(-1, 1)
reg = LinearRegression().fit(x, y)
print("一元回归方程为:  Y = %.5fX + (%.5f)" % (reg.coef_[0], reg.intercept_[0]))
print("R平方为: %s" % reg.score(x, y))

plt.scatter(x, y,  color='black')
plt.plot(x, reg.predict(x), color='red', linewidth=1)
plt.show()