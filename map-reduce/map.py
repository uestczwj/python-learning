#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:56:56 2018

@author: zwj
"""

#举例说明,比如我们有一个函数 f(x)=x * x ,要把这个函数作用在一个 list [1,2, 3, 4, 5, 6, 7, 8, 9] 上,就可以用 map() 实现如下:
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

#不需要 map() 函数,写一个循环,也可以计算出结果:
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
    
print(L)

#的确可以,但是,从上面的循环代码,能一眼看明白“把 f(x)作用在 list的每一个元素并把结果生成一个新的 list”吗?