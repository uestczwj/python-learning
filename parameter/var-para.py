# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
        
    return sum
#但是调用的时候,需要先组装出一个 list 或 tuple:
print(calc([1, 2, 3]))

print(calc((1, 3, 5, 7)))

#如果利用可变参数,调用函数的方式可以简化成这样:

def calc(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
        
    return sum

sum = calc(1, 2, 3, 4)
print('1 + 2 + ... + 4   =', sum)

sum = calc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('1 + 2 + ... + 10  =', sum)

#如果已经有一个 list 或者 tuple,要调用一个可变参数怎么办?可以前面加一个 * 号,把 list 或 tuple 的元素变成可变参数传进去
nums = range(1, 101)
#*nums 表示把 nums 这个 list 的所有元素作为可变参数传进去。这种写法相当有用,而且很常见
sum = calc(*nums)
print('1 + 2 + ... + 100 =', sum)

