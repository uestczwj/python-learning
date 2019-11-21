import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')

#filter(保留满足条件的项)
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), index=['mouse', 'rabbit'], columns=['one', 'two', 'three'])
print_with_info(df, "-------------- data of dataframe ------------")
"""
        one  two  three
mouse     1    2      3
rabbit    4    5      6
"""

df1 = df.filter(items=['one', 'three'])
print_with_info(df1, "df1 = df.filter(items=['one', 'three'])")
'''
         one  three
mouse     1      3
rabbit    4      6
'''

# select columns by regular expression
df2 = df.filter(regex='e$', axis=1)
print_with_info(df2, "df2 = df.filter(regex='e$', axis=1)")
'''
         one  three
mouse     1      3
rabbit    4      6
'''

df2 = df.filter(regex='^t', axis=1)
print_with_info(df2, "df2 = df.filter(regex='^t', axis=1)")
'''
        two  three
mouse     2      3
rabbit    5      6
'''

# select rows containing 'bbi'
df3 = df.filter(like='bbi', axis=0)
print_with_info(df3, "df3 = df.filter(like='bbi', axis=0)")
'''
         one  two  three
rabbit    4    5      6
'''
