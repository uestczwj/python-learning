#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:15:24 2018

@author: zwj

range, zip, enumerate

"""

print('function range demo : \n')
numbers = list(range(1, 11))
print('list(range(1, 11) = ', numbers)

names = ['zwj', 'hjj', 'zjh', 'kkk']
ages =  [22,     21,    23,    20]

print('\n function enumerate demo : \n')
for index, name in enumerate(names):
    print("The {}th name is {}".format(index, name))
    
print('\n')    
for index, age in enumerate(ages):
    print("The {}th age is {}".format(index, age))


d = zip(names, ages)
print('zip(names, ages) = ', dict(d))

print('\n function zip demo : \n')
for name, age in zip(names, ages):
    print("{}'s age is {}".format(name, age))    
    
    