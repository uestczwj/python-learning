import pandas as pd #数据分析
from   pandas import Series,DataFrame
import matplotlib.pyplot as plt

data_train = pd.read_csv("train.csv")
print(data_train)

print(data_train.columns)

#然后我们再来看看各种舱级别情况下各性别的获救情况
fig=plt.figure()
fig.set(alpha=0.65) # 设置图像透明度，无所谓

plt.title(u"根据舱等级和性别的获救情况")

"""
            *pos* is a three digit integer, where the first digit is the
            number of rows, the second the number of columns, and the third
            the index of the subplot. i.e. fig.add_subplot(235) is the same as
            fig.add_subplot(2, 3, 5). Note that all integers must be less than
            10 for this form to work.

            If no positional arguments are passed, defaults to (1, 1, 1).
"""
ax1=fig.add_subplot(1, 4, 1)
data_train.Survived[data_train.Sex == 'female'][data_train.Pclass != 3].value_counts().plot(kind='bar', label="female highclass", color='#FA2479')
ax1.set_xticklabels([u"获救", u"未获救"], rotation=0)
ax1.legend([u"女性/高级舱"], loc='best')

ax2=fig.add_subplot(1, 4, 2, sharey=ax1)
data_train.Survived[data_train.Sex == 'female'][data_train.Pclass == 3].value_counts().plot(kind='bar', label='female, low class', color='pink')
ax2.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u"女性/低级舱"], loc='best')

ax3=fig.add_subplot(1, 4, 3, sharey=ax1)
data_train.Survived[data_train.Sex == 'male'][data_train.Pclass != 3].value_counts().plot(kind='bar', label='male, high class',color='lightblue')
ax3.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u"男性/高级舱"], loc='best')

ax4=fig.add_subplot(1,4, 4, sharey=ax1)
data_train.Survived[data_train.Sex == 'male'][data_train.Pclass == 3].value_counts().plot(kind='bar', label='male low class', color='steelblue')
ax4.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u"男性/低级舱"], loc='best')

plt.show()
