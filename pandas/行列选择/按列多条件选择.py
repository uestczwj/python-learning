import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->\n')

# 列操作
dic1 = {'name':['小明','小红','狗蛋','铁柱'],'age':[17,20,5,40],'gender':['男','女','女','男']}
df3 = pd.DataFrame(dic1, index=range(1,5))
print_with_info(df3, 'df3')
"""
---------df3------------------
  name  age gender
1   小明   17      男
2   小红   20      女
3   狗蛋    5      女
4   铁柱   40      男
"""
df3.loc[df3['age'] == 5, 'age'] += 10
print_with_info(df3, 'df3 (after modify age ==5')
'''
  name  age gender
1   小明   17      男
2   小红   20      女
3   狗蛋   15      女
4   铁柱   40      男
'''

print_with_info(type(df3['name']), "type(df3['name'])")
print_with_info(df3['name'], "取出某一列的值(不显示列名称)")   #type : series
'''
1    小明
2    小红
3    狗蛋
4    铁柱
Name: name, dtype: object'''

print_with_info(type(df3.name), "type(df3.name)")
'''<class 'pandas.core.series.Series'>'''

print_with_info(df3.name, "df3.name的所有值")                       #type : series, df3.name与df3['name']相同
'''
1    小明
2    小红
3    狗蛋
4    铁柱
Name: name, dtype: object'''

print_with_info(df3.name[df3.age >= 20], "df3.name[df3.age >= 20]的所有值")
'''
2    小红
4    铁柱
Name: name, dtype: object'''



print_with_info(df3.loc[1, 'name'], "获取行列交叉点的值")  #type : str

print("#根据其它的属性选出一列(保留Dataframe属性)")
print_with_info(df3[['name']], "取出某一列构成Dataframe")
'''
  name
1   小明
2   小红
3   狗蛋
4   铁柱'''

print_with_info(df3[['name', 'age']], "取出某几列的构成的Dataframe")   #type : Dataframe
'''
  name  age
1   小明   17
2   小红   20'''

# df3[['name']][df3.age >= 20] <--->  df3.loc[df3.age >= 20, ['name', 'age']]
print_with_info(df3['name'][df3.age >= 20], "df3['name'][df3.age >= 20]")
print_with_info(df3[['name']][df3.age >= 20], "df3[['name']][df3.age >= 20]")
print_with_info(df3.loc[df3.age >= 20, ['name']], "df3.loc[df3.age >= 20, ['name']]")   # recommend method

print_with_info(df3.loc[df3.age >= 20, ['name', 'age']], "df3.loc[df3.age >= 20, ['name', 'age']]")

