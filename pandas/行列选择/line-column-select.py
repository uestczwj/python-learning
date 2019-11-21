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

