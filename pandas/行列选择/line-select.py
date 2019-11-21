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
1.2 行选择 : 得到一个Series    (iloc : index location), iloc只能用数字索引，不能用索引名
"""
print("1.2 行选择 iloc: 得到一个Series")

for i in range(4):
    print_with_info(df.iloc[i], "df.iloc[{}]".format(i))
