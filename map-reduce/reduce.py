#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:54:02 2018

@author: zwj
"""


#整理成一个 str2int 的函数就是:
from functools import reduce

def str2int(s):
    def fn(x, y):
       return x * 10 + y
    
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))

str = input('Plese enter a string number : ')

num = str2int(str)

print('it is :', num)
    
#还可以用 lambda 函数进一步简化成:
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7':7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

str = input('Plese enter a string number : ')

num = str2int(str)

print('it is :', num)

