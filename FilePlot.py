import numpy as np
import matplotlib.pyplot as plt

filename = '/home/admin/share/upload/waveData.txt'

with open(filename) as f:
    original_data = f.readlines()


data = []

for i in original_data:
    d = i.split('\t')
    #if len(d) == 10:
    for j in d:
        try :
            num=float(j)
        except:
            print("当前值是 换行符")
        else:
            data.append(num)



data_Np = np.array(data)

length = data_Np.shape[0]

did = length%8

if did == 0 :
    data2plot = data_Np[:]
else:
    data2plot = data_Np[:-did]

data2plot.shape=(-1,8)

#data_N = data_Np / 1000000
"""
for i in range(8):
    name = 'Channel ' + str(i)
    plt.figure(name)
    plt.plot(data2plot[:, i])
    
"""

plt.figure("Data Plot channel 1-4 ")
for i in range(1,5):
    name = 'Channel ' + str(i)
    plt.subplot(4,1,i)
    plt.plot(data2plot[:,i-1])
    plt.title(name)



plt.figure("Data Plot channel 5-8")
for i in range(1,5):
    name = 'Channel ' + str(i+4)
    plt.subplot(4,1,i)
    plt.plot(data2plot[:,i+4-1])
    plt.title(name)

#plt.figure('channel 0')
#plt.plot(data2plot[:,0])


#np.savetxt("ch1.txt",data_Np,fmt='%f',delimiter=',')

plt.show()