#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:41:43 2018

@author: zwj
"""


min = 0
max = 100

while True:
    str = input('Please enter a integer number(q or Q to quit) : ')
    if str == 'q' or str == 'Q': break
    
    a = int(str)
    
    if (min <= a < max):
        print('{} is in range({}, {})'.format(a, min, max))
    else:
        print('{} is not in range({}, {})'.format(a, min, max)) 
        


