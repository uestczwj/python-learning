import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->')

df = pd.DataFrame({'A' : range(5), 'B' : range(5, 10), 'C': range(10, 15)})
print_with_info(df, "df = pd.DataFrame({'A' : range(5), 'B' : range(5, 10), 'C': range(10, 15)})")
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
print_with_info(a_dummies, "a_dummies = pd.get_dummies(df['A'], prefix='A')")
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
print_with_info(df, "df = pd.concat([df, a_dummies], axis=1)")
"""
   A  B   C  A_0  A_1  A_2  A_3  A_4
0  0  5  10    1    0    0    0    0
1  1  6  11    0    1    0    0    0
2  2  7  12    0    0    1    0    0
3  3  8  13    0    0    0    1    0
4  4  9  14    0    0    0    0    1
"""
