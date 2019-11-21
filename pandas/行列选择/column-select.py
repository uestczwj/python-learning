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