import pandas as pd
import numpy  as np

def print_with_info(info, data):
    print('-----------' + info + '--------------- : ')
    print(data)

PassengerId = list(range(1, 11))
#               x       x                        x      x       x
y_cv        = [1,       1,      1,      0,      0,      1,      1,    1,     0,     0]
predictions = [0,       1,      1,      0,      1,      1,      1,    1,     0,     1]
Name        = ['zwj', 'file', 'zwjfile', 'hjj', 'kxl', 'aaa', 'bbb', 'ccc', 'ddd', 'eee']
origin_data_train =  pd.DataFrame({'PassengerId' : PassengerId, 'Name' : Name})

#先去第1,2个,再取4,5,6共5个元素
split_cv =  origin_data_train[0:2]
split_cv = pd.concat([split_cv, origin_data_train[4:7]])

print_with_info('split_cv', split_cv)

t1 = [1, 1, 0, 1, 1]  #取所有数据的0,1,4,5,6五个数据
t2 = [0, 1, 1, 1, 1]

a = np.array(t1)
b = np.array(t2)

element_no_equal = (a != b)
print_with_info('element_no_equal', element_no_equal)

print_with_info('split_cv[element_no_equal]', split_cv[element_no_equal])

bad_cases = split_cv[element_no_equal]['Name'].values
print_with_info("bad_cases", bad_cases)

names_in_bad_cases = origin_data_train['Name'].isin(bad_cases)
print_with_info('names_in_bad_cases', names_in_bad_cases)

all_in_bad_cases = origin_data_train.loc[names_in_bad_cases]
print_with_info('all_in_bad_cases', all_in_bad_cases)

print()
