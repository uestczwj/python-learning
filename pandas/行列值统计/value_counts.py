import numpy    as np
import pandas   as pd
import matplotlib.pyplot as plt

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')


dic = {'no':['94141-101','94141-102','94141-103','94141-104','94141-105'], 'name':['小明','小红','狗蛋','铁柱', 'zwj'],'age':[10,20,5,40, 45],'gender':['Male','Female','Female','Male','Male']}
df  = pd.DataFrame(dic, index = range(1, 6))
print_with_info(df, 'df = pd.DataFrame(dic, index=range(1, 6))')

df1 = df[0:2]
df = pd.concat([df, df1], ignore_index=True)   # ignore_index=True : index自动生成； ignore_index=False : index保持concat前的不变化
print_with_info(df, 'df = pd.concat([df, df1])')

print_with_info(df.name.value_counts(), "df.name.value_counts()")
"""
小明     2
小红     2
zwj    1
铁柱     1
狗蛋     1
"""

print_with_info(df.gender.value_counts(), "df.gender.value_counts()")
"""
Male      4
Female    3
"""


"""
#  按列"gender"的不同值(男性和女性),分别统计男性和女性的总人数, 得到一个Series
"""

df.gender.value_counts().plot(kind='bar')
plt.show()

females = df.gender[df.gender == 'Female'].value_counts()
males   = df.gender[df.gender == 'Male'].value_counts()
print_with_info(males, "males")
print_with_info(females, "females")

fig = plt.figure()
fig.set(alpha=0.2)
df = pd.DataFrame({'Male' : males, 'Female' : females});
df.plot(kind = 'bar')
plt.show()


