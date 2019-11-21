import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print('---------------------------------------------->\n')

# 创建一个Dataframe
dic = {'no':['94141-101','94141-102','94141-103','94141-104'], 'name':['小明','小红','狗蛋','铁柱'],'age':[17,20,5,40],'gender':['男','女','女','男']}
df  = pd.DataFrame(dic, index = range(1, 5))
print_with_info(df, 'df = pd.DataFrame(dic, index=range(1, 5))')

# 取出某几列构成的Dataframe
df1 = df[['age', 'gender']]
print_with_info(df1, "df1 = df[['age', 'gender']]")

# 删除某几列
df = df.drop(['age', 'gender'], axis=1)
print_with_info(df, "df = df.drop([''age', gender'], axis=1)")

# 在列上拼接上另一个Dataframe
df = pd.concat([df, df1], axis=1)
print_with_info(df, 'df = df.concat([df, df1])')

# 取出某几行构成的Dataframe: 行索引编号(从0开始)
df2 = df.iloc[0:2]    #第一行和第二行
print_with_info(df2, 'df2 = df[0:2, :]')

# 删除某几行(1,2是行标签, 不是行索引编号)
df = df.drop([1, 2])   # 行索引标签
print_with_info(df, "df = df.drop(df[11:12], axis=0)")

# 在列上拼接上另一个Dataframe
df = pd.concat([df2, df], axis=0)
print_with_info(df, 'df = pd.concat([df, df2], axis=0)')

#修改满足条件的项的值
temp = df.loc[df['age'] < 20, 'age']
print_with_info(temp, "df.loc[df['age'] < 20, 'age']")

#修改满足条件的项的值
df.loc[df['age'] < 20, 'age'] = 20
print_with_info(df, "df.loc[df['age'] < 20, 'age'] = 20")

#生成gender的Hot  Code
gender_dummies = pd.get_dummies(df['gender'], prefix='gender')
print_with_info(gender_dummies, "gender_dummies = pd.get_dummies(df['gender'], prefix='gender')")

df = pd.concat([df, gender_dummies], axis=1)
print_with_info(df, 'df = pd.concat([df, gender_dummies], axis=1)')

df = df.drop(['gender'], axis = 1)
print_with_info(df, "df = df.drop(['gender'], axis = 1)")

for col in df.columns:
    series = df[col]
    print_with_info(series, 'series')

print_with_info(df.index, "df.index")

print_with_info(df.to_numpy(), "df.to_numpy()")


