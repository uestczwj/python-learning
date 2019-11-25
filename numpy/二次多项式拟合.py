import numpy
import matplotlib.pyplot as plt

def polyfit(x, y, degree):
    results = {}
    coeffs = numpy.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot #准确率
    return results

x=[ 1 ,2  ,3 ,4 ,5 ,6]
y=[ 2.5 ,3.51 ,4.45 ,5.52 ,6.47 ,7.2]
z1 = polyfit(x, y, 2)
print(z1)   # y = a *pow(x, 2) + b * x + c
print("y =  {} *pow(x, 2) + {} * x + {}".format(z1['polynomial'][0], z1['polynomial'][1], z1['polynomial'][2]))

for i in range(len(x)):
    y_value = z1['polynomial'][0] * x[i] * x[i] + z1['polynomial'][1] * x[i] + z1['polynomial'][0]
    diff = y_value - y[i]
    print("diff = {}".format(diff))

plt.plot(x, y)
plt.show()

