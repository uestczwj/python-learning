import numpy    as np
import pandas   as pd
import matplotlib.pyplot as plt

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')

"""
分组统计, 注意: groupby([]).sum()只对数字列进行统计
"""
print("------分组统计, 注意: groupby([]).sum()只对数字列进行统计-----\n" * 3)

df1 = pd.DataFrame() # columns 为列名 并且必须是list类型

df1["grade"]    = ['1',   '1',    '1',  '1']
df1["name"]     = ["hjj", "jxl", "kxl", "zwj"]
df1["c++"]      = [93,    84,     75,    93]
df1["math"]     = [73,    83,     79,    73]
df1["python"]   = [78,    86,     85,    83]
df1["java"]     = [89,    82,     95,    90]

df2 = pd.DataFrame() # columns 为列名 并且必须是list类型

df2["grade"]    = ['2',    '2',   '2',   '2']
df2["name"]     = ["hjj", "jxl", "kxl", "zwj"]
df2["c++"]      = [88,    83,     85,    83]
df2["math"]     = [85,    87,     89,    79]
df2["python"]   = [87,    88,     75,    88]
df2["java"]     = [84,    83,     85,    80]

df = pd.concat([df1, df2], ignore_index=True)
print_with_info(df, "df")

df1 = df.groupby(["grade"]).sum() # 可以通过as_index指定分组项要不要成为索引， 默认为True
print_with_info(df1, 'df.groupby(["grade"]).sum()')
print_with_info(df1["c++"], 'df1["c++"]')

df1 = df.groupby(["name"]).sum() # 可以通过as_index指定分组项要不要成为索引， 默认为True
print_with_info(df1, 'df.groupby(["name"]).sum()')
print_with_info(df1["c++"], 'df1["c++"]')

