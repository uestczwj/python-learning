#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 10:47:32 2018

@author: zwj
"""

'''######## map funciton  ########'''
def square(a):
    return a * a

numbers     = list(range(1, 11))
square_num  = list(map(square, numbers))

print(square_num)
'''######## map funciton  ########'''


'''######## reduce funciton  ########'''
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers = reduce(lambda x,y : x * 10 +y, numbers)
print(numbers)

'''######## str2int funciton  ########'''
from functools import reduce

def char2num(s):
    str_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8': 8, '9': 9}
    return str_number_dict[s]

def str2int(s):  
    numbers = list(map(char2num, s))
    return reduce(lambda x, y: x * 10 + y, numbers)    

print(str2int("1234567"))
    
'''######## reduce funciton  ########'''


'''######## filter funciton  ########'''
def check_postive(a):
    return a > 0

numbers = [1, -2, 3, -4, 3, 4, -6, -7]

postive_numbers = filter(check_postive, numbers)
print(list(postive_numbers))

'''######## filter funciton  ########'''


