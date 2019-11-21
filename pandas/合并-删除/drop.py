import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')

lines_count    = 3
columns_count  = 3

df = pd.DataFrame({'A' : range(5), 'B' : range(5, 10), 'C': range(10, 15)})
print_with_info(df, "df = pd.DataFrame({'A' : range(5), 'B' : range(5, 10), 'C': range(10, 15)})")
'''
   A  B   C
0  0  5  10
1  1  6  11
2  2  7  12
3  3  8  13
4  4  9  14'''

#删除行---删除行---删除行---删除行---删除行---删除行---删除行---删除行---
df_drop_line = df.drop([0], axis=0)  # 等同于 df_drop_line = df.drop([0])
print_with_info(df_drop_line, "df_drop_line = df.drop([0], axis=0)")
"""
   A  B   C
1  1  6  11
2  2  7  12
3  3  8  13
4  4  9  14
"""

#删除列---删除列---删除列---删除列---删除列---删除列---删除列---
df_drop_column = df.drop(['A'], axis=1)
print_with_info(df_drop_column, "df_drop_column = df.drop(['A'], axis=1)")
"""
   B   C
0  5  10
1  6  11
2  7  12
3  8  13
4  9  14
"""

