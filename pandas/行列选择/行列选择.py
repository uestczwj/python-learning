import numpy    as np
import pandas   as pd

def print_with_info(data, info):
    print('\n<--------- ' + info + '------------------')
    print(data)
    print(type(data))
    print('---------------------------------------------->')


dic = {'no':['94141-101','94141-102','94141-103','94141-104'], 'name':['小明','小红','狗蛋','铁柱'],'age':[10,20,5,40],'gender':['Male','Female','Female','Male']}
df  = pd.DataFrame(dic, index = range(1, 5))
print_with_info(df, 'df = pd.DataFrame(dic, index=range(1, 5))')

"""  
1.1 行选择 : 得到一个Dataframe    
"""
print("1.1 行选择 : 得到一个Dataframe ")
#通过[ ]选择，对行进行切片,得到的还是一个Dataframe
print_with_info(df[0:3], "df[0:3]")

"""  
1.2 行选择 : 得到一个Series    
"""
print("1.2 行选择 : 得到一个Series")
print_with_info(df.iloc[1], "df.iloc[1]")

"""  
2.1 列选择 : 得到一个Dataframe 
"""
print("2.1 列选择 : 得到一个Dataframe")
print_with_info(df[['no', 'name']], "df[['no', 'name']]")
print_with_info(df.loc[:, ['no', 'name']], "df.loc[:, ['no', 'name']]")

"""
2.2 选择某一列 : 得到一个Series 
"""
print("2.2 选择某一列 : 得到一个Series")
print_with_info(df.name, "df.name")
print_with_info(df['name'], "df['name']") # df.name 与 df['name'] 相同

"""
2.3 根据另一列的值选择某一列 : 得到一个Series 
"""
print("2.3 根据另一列的值选择某一列 : 得到一个Series")
print_with_info(df[['name', 'age', 'gender']][df.age >= 10], "df[['name', 'age']][df.age >= 10]")
print_with_info(df.name[df.age == 10], "df.name[df.age == 10]")
print_with_info(df.name[df.age >= 10][df.gender == 'Male'], "df.name[df.age >= 10][df.gender == 'Male']")

"""  
3. 行列同时选择 : 得到一个Dataframe          
"""
print("3. 行列同时选择 : 得到一个Dataframe")
print_with_info(df.loc[0:3, ['no', 'name']], "df.loc[0:3, ['no', 'name']]")

""" 
4. 行列交叉点值选择 : 得到一个标量值               
"""
print("4. 行列交叉点值选择 : 得到一个标量值")
print_with_info(df.iloc[1, 1], "df.iloc[1, 1]")
print_with_info(df.iat[1, 1], "df.iat[1, 1]")  #快速访问标量(等价于之前的方法)：

