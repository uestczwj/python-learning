#Access a group of rows and columns by label(s) or a boolean array.

import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print('---------------------------------------------->\n')

#行操作: loc或iloc
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
print_with_info(df, "df")
#df必须明确指定了行和列的label
print_with_info(df.loc['cobra', 'shield'], "df.loc['cobra', 'shield']")
#按行编号对应boolean列表的索引值, 取出行编号对应为True的行
print_with_info(df.loc[[False, False, False]], "df.loc[[False, False, False]]")  #一个都不取
print_with_info(df.loc[[False, False, True]], "df.loc[[False, False, True]]")
print_with_info(df.loc[[False, True, False]], "df.loc[[False, True, False]]")
print_with_info(df.loc[[False, True, True]], "df.loc[[False, True, True]]")
print_with_info(df.loc[[True, False, False]], "df.loc[[True, False, False]]")
print_with_info(df.loc[[True, False, True]], "df.loc[[True, False, True]]")
print_with_info(df.loc[[True, True, False]], "df.loc[[True, True, False]]")
print_with_info(df.loc[[True, True, True]], "df.loc[[True, True, True]]")       #三个都取

df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['one', 'two', 'thr'], columns=list('abcd'))
print(df)
print("----------------")
df['a']  # 取a列
df[['a', 'b']]  # 取a、b列

# ix可以用数字索引，也可以用index和column索引
df.iloc[0]  # 取第0行
df.iloc[0:1]  # 取第0行
df.loc['one':'two']  # 取one、two行
