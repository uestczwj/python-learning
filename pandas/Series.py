import numpy    as np
import pandas   as pd

l = range(6)
s = pd.Series(l)
print(s)
"""
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int64
"""
s = pd.Series(l, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s)
"""
a    0
b    1
c    2
d    3
e    4
f    5
dtype: int64
"""

d = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(d)
print(s)
"""
a    1
b    2
c    3
dtype: int64
"""

print(s.index)
"""
Index(['a', 'b', 'c'], dtype='object')
"""

print(pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))
"""
a    5.0
b    5.0
c    5.0
d    5.0
e    5.0
dtype: float64
"""