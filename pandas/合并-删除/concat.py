import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')

lines_count    = 3
columns_count  = 3

row_index_1 = range(1, 4)
row_index_2 = range(4, 7)

#行合并---行合并---行合并---行合并---行合并---行合并---行合并---行合并---行合并---行合并---
print('DataFrame concat  on line : different index, same column, axis=0 (this is default)')
df1 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=row_index_1, columns=['A', 'B', 'C'])
df2 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=row_index_2, columns=['A', 'B', 'C'])

print_with_info(df1, "df1")

print_with_info(df2, "df2")

df = pd.concat([df1, df2])  #same to : df = pd.concat([df1, df2], axis=0)
print_with_info(df, "pd.concat([df1, df2])")
"""
          A         B         C
1  1.024702  0.237990 -2.510329
2 -0.393099  0.804742  0.553678
3 -1.219761  0.498994  0.761770
4  0.703909  2.103649  1.327072
5  0.873561  1.679320 -0.325726
6  2.038983  0.668668  0.165263
"""

#列合并---列合并---列合并---列合并---列合并---列合并---列合并---列合并---列合并---列合并---
print('DataFrame concat  on column : same index, different column, axis=1')
df1 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=row_index_1, columns=['A', 'B', 'C'])
df3 = pd.DataFrame(np.random.randn(lines_count, columns_count), index=row_index_1, columns=['D', 'E', 'F'])
df = pd.concat([df1, df3], axis=1)
print_with_info(df, "pd.concat([df1, df3], axis=1)")
"""
          A         B         C         D         E         F
1  1.950923  0.259569 -0.227687  0.662314 -0.073797 -0.560758
2 -0.175153 -0.519101 -0.949789  0.498428  2.038896 -1.339646
3 -0.139725  0.441338 -0.636171  0.208407  1.248342  0.091605
"""
