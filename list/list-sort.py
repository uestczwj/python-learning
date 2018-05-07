#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:12:09 2018

@author: zwj
"""

print('1. list sort is in-place sort')  
print('2. sorted is copy sort  ')


'''######## list sort  ########'''
li = list(range(0, 11))

for i in li:
    if li[i] % 2 == 0:
        li[i] = -li[i]

print('before list.sort, li=', li)
print('li.sort()=', li.sort())
print('after list.sort, li=', li)
'''######## list sort  ########'''

'''######## sorted funciton  ########'''
numbers = [1, -2, 3, -4, 3, 4, -6, -7]
print('before sorted(numbers), numbers = ', numbers)
print('sorted(numbers) = ', sorted(numbers))
print('after sorted(numbers), numbers = ', numbers)
print('sorted(numbers) by abs= ', sorted(numbers, key=abs))
'''######## sorted funciton  ########'''


numbers = [1, -2, 3, -4, 3, 4, -6, -7]

is_sort_equal = (numbers.sort() == sorted(numbers))
print('is_sort_equal = ', is_sort_equal)

