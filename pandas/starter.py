'''
pandas取dataframe特定行/列
分类: Pandas
标签: pandas
1. 按列取、按索引/行取、按特定行列取
'''

import numpy as np
from pandas import DataFrame
import pandas as pd
 
 
df=DataFrame(np.arange(12).reshape((3,4)),index=['one','two','thr'],columns=list('abcd'))
print(df)
print("----------------")
df['a']#取a列
df[['a','b']]#取a、b列
 
#ix可以用数字索引，也可以用index和column索引
df.iloc[0]#取第0行
df.iloc[0:1]#取第0行
df.loc['one':'two']#取one、two行
df.iloc[0:2,0]#取第0、1行，第0列
df.loc[['one','two'], 'a']#取第0行，a列
df.loc[['one','two'], ['a', 'b', 'c']]#取第0、1行，abc列
df.loc['one':'two','a':'c']#取one、two行，abc列
df.iloc[0:2,0:1]#取第0、1行，第0列
df.iloc[0:2,0:2]#取第0、1行，第0、1列
 
#loc只能通过index和columns来取，不能用数字
df.loc['one','a']#one行，a列
df.loc['one':'two','a']#one到two行，a列
df.loc['one':'two','a':'c']#one到two行，a到c列
df.loc['one':'two',['a','c']]#one到two行，ac列
 
#iloc只能用数字索引，不能用索引名
df.iloc[0:2]#前2行
df.iloc[0]#第0行
df.iloc[0:2,0:2]#0、1行，0、1列
df.iloc[[0,2],[1,2,3]]#第0、2行，1、2、3列
 
#iat取某个单值,只能数字索引
df.iat[1,1]#第1行，1列
#at取某个单值,只能index和columns索引
df.at['one','a']#one行，a列

'''
2. 按条件取行
选取等于某些值的行记录 用 ==
df.loc[df[‘column_name’] == some_value]

#选取某列是否是某一类型的数值 用 isin
df.loc[df[‘column_name’].isin(some_values)]
 
#多种条件的选取 用 &
df.loc[(df[‘column’] == some_value) & df[‘other_column’].isin(some_values)]
 
#选取不等于某些值的行记录 用 ！=
df.loc[df[‘column_name’] != some_value]
 
#isin返回一系列的数值,如果要选择不符合这个条件的数值使用~
df.loc[~df[‘column_name’].isin(some_values)]
'''
#3. 取完之后替换

print(df)
print('-------------------------')

df = pd.DataFrame({"id": [25,53,15,47,52,54,45,9], "sex": list('mfmfmfmf'), 'score': [1.2, 2.3, 3.4, 4.5,6.4,5.7,5.6,4.3],"name":['daisy','tony','peter','tommy','ana','david','ken','jim']})
print(df)
print('-------------------------')

#将男性(m)替换为1，女性(f)替换为0
#方法1：

df.loc[df['sex']=='f','sex']=0
df.loc[df['sex']=='m','sex']=1

#注：在上面的代码中，逗号后面的‘sex’起到固定列名的作用
#方法2：
# error : A value is trying to be set on a copy of a slice from a DataFrame
#df['sex'][df['sex']=='m']=1
#df['sex'][df['sex']=='f']=0

print(df)