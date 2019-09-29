import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print(info)
    print(data)

lines_count    = 3
columns_count  = 3

dates1 = pd.date_range('20130101', periods=lines_count)
print(dates1)
"""
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03'], dtype='datetime64[ns]', freq='D')
"""

df1 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=dates1, columns=['A', 'B', 'C'])
print_with_info(df1, "------------------data of dataframe------------------")
"""
                   A         B         C
2013-01-01  2.135824  1.457449  0.500426
2013-01-02 -1.933266 -1.394927 -0.351620
2013-01-03  1.152293  0.052140  0.702374
"""
print("------------------Info of dataframe------------------")
df1.info()
print_with_info(df1.describe(), "------------------Describe of dataframe------------------")

dates2 = pd.date_range('20130104', periods=lines_count)
print(dates2)
"""
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03'], dtype='datetime64[ns]', freq='D')
"""

#行合并---行合并---行合并---行合并---行合并---行合并---行合并---行合并---行合并---行合并---
print('DataFrame concat  on line : differt index, same column, axis=0 (this is default)')
df1 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=dates1, columns=['A', 'B', 'C'])
df2 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=dates2, columns=['A', 'B', 'C'])

df = pd.concat([df1, df2])  #same to : df = pd.concat([df1, df2], axis=0)
print(df)
"""
                   A         B         C
2013-01-01 -1.147462 -0.208490 -0.512215
2013-01-02  1.825054 -0.310802 -0.869684
2013-01-03 -1.780141 -1.692715 -0.415956
2013-01-04  0.114022  0.816112 -2.060466
2013-01-05 -0.473986 -1.226916 -0.322938
2013-01-06 -0.665206 -0.686250 -0.882400
"""

#列合并---列合并---列合并---列合并---列合并---列合并---列合并---列合并---列合并---列合并---
print('DataFrame concat  on column : same index, differt column, axis=1')
df1 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=dates1, columns=['A', 'B', 'C'])
df3 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=dates1, columns=['D', 'E', 'F'])
df = pd.concat([df1, df3], axis=1)
print(df)
"""
                   A         B         C         D         E         F
2013-01-01  1.532415  0.177206  1.312361 -0.316278  0.152167  1.479065
2013-01-02  1.258986 -0.184694 -0.989352  0.311237 -0.940460 -1.615886
2013-01-03 -0.902858 -1.165769 -0.837366  1.955709  0.467783  0.384324
"""

df = pd.DataFrame({'A' : range(5), 'B' : range(5, 10), 'C': range(10, 15)})
print(df)
"""
   A  B   C
0  0  5  10
1  1  6  11
2  2  7  12
3  3  8  13
4  4  9  14
"""

#HotCode---HotCode---HotCode---HotCode---HotCode---HotCode---HotCode---HotCode---
a_dummies = pd.get_dummies(df['A'], prefix='A')
print(a_dummies)
"""
   A_0  A_1  A_2  A_3  A_4
0    1    0    0    0    0
1    0    1    0    0    0
2    0    0    1    0    0
3    0    0    0    1    0
4    0    0    0    0    1
"""

# 列拼接---列拼接---列拼接---列拼接---列拼接---列拼接---列拼接---列拼接---
df = pd.concat([df, a_dummies], axis=1)
print(df)

"""
   A  B   C  A_0  A_1  A_2  A_3  A_4
0  0  5  10    1    0    0    0    0
1  1  6  11    0    1    0    0    0
2  2  7  12    0    0    1    0    0
3  3  8  13    0    0    0    1    0
4  4  9  14    0    0    0    0    1
"""

#删除列---删除列---删除列---删除列---删除列---删除列---删除列---
df_drop_column = df.drop(['A'], axis=1)
print(df_drop_column)
"""
   B   C  A_0  A_1  A_2  A_3  A_4
0  5  10    1    0    0    0    0
1  6  11    0    1    0    0    0
2  7  12    0    0    1    0    0
3  8  13    0    0    0    1    0
4  9  14    0    0    0    0    1
"""

#删除行---删除行---删除行---删除行---删除行---删除行---删除行---删除行---
df_drop_line = df.drop([0], axis=0)  # df_drop_line = df.drop([0])
print(df_drop_line)
"""
   A  B   C  A_0  A_1  A_2  A_3  A_4
1  1  6  11    0    1    0    0    0
2  2  7  12    0    0    1    0    0
3  3  8  13    0    0    0    1    0
4  4  9  14    0    0    0    0    1
"""

#filter(保留满足条件的项)
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), index=['mouse', 'rabbit'], columns=['one', 'two', 'three'])
print_with_info(df, "-------------- data of dataframe ------------")
"""
        one  two  three
mouse     1    2      3
rabbit    4    5      6
"""

df1 = df.filter(items=['one', 'three'])
print_with_info(df1, "-------  items = ['one', 'three']---------")
'''
         one  three
mouse     1      3
rabbit    4      6
'''

# select columns by regular expression
df2 = df.filter(regex='e$', axis=1)
print_with_info(df2, "-------  regex='e$'  ----------")
'''
         one  three
mouse     1      3
rabbit    4      6
'''

df2 = df.filter(regex='^t', axis=1)
print_with_info(df2, "-------  regex='^t'  ----------")
'''
        two  three
mouse     2      3
rabbit    5      6
'''

# select rows containing 'bbi'
df3 = df.filter(like='bbi', axis=0)
print_with_info(df3, "-------  like='bbi'  ----------")
'''
         one  two  three
rabbit    4    5      6
'''

df1 = pd.DataFrame(np.array([[1,2,3]]), index=['mouse'], columns=['one', 'two', 'three'])
df2 = pd.DataFrame({'one':[1], 'two':[2], 'three':[3]}, index=['wolf'])
print_with_info(df1, '---df2----')

df3 = pd.concat([df1, df3])
print_with_info(df3, "-------  pd.concat([df3, df2])  ----------")

df3 = pd.concat([df2, df3])
print_with_info(df3, "-------  pd.concat([df3, df2])  ----------")
