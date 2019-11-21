import numpy    as np
import pandas   as pd
import matplotlib.pyplot as plt

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')

"""
分组统计 ()
"""
df1 = pd.DataFrame() # columns 为列名 并且必须是list类型

df1["grade"]     = [1,    1,      1,     1]
df1["name"]     = ["hjj", "jxl", "kxl", "zwj"]
df1["c++"]      = [93,    84,     75,    93]
df1["math"]     = [73,    83,     79,    73]
df1["python"]   = [78,    86,     85,    83]
df1["java"]     = [89,    82,     95,    90]

print_with_info(df1.describe(), "df1.describe()")

print_with_info(df1.info(), "df1.info()")

print_with_info(df1.head(3), "df1.head()")

print_with_info(df1.tail(3), "df1.tail()")