#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:06:36 2018

@author: zwj
"""

def power(x, n=2):
    pow   = x
    while n > 1:
        pow = pow * x
        n -= 1
    
    return pow
    

pow = power(4)
print('{}^{} = {}'.format(4, 2, pow))

pow = power(5)
print('{}^{} = {}'.format(5, 2, pow))

pow = power(5, 4)
print('{}^{} = {}'.format(5, 4, pow))




