#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:18:42 2018

@author: zwj
"""

'''如果要限制关键字参数的名字,就可以用命名关键字参数,例如,只接收 city 和 job 作为关键字参数。
这种方式定义的函数如下:'''
def person(name, age, *, city, job):
    print(name, age, city, job)
    
#和关键字参数 **kw 不同,命名关键字参数需要一个特殊分隔符 * , * 后面的参数被视为命名关键字参数。
#调用方式如下:
person('Jack', 24, city='Beijing', job='Engineer')

#命名关键字参数必须传入参数名,这和位置参数不同。如果没有传入参数名,调用将报错:
#person('Jack', 24, 'Beijing', 'Engineer')   #TypeError: person() takes 2 positional arguments but 4 were given

#由于调用时缺少参数名 city 和 job ,Python 解释器把这 4 个参数均视为位置参数,但 person() 函数仅接受 2 个位置参数。
#命名关键字参数可以有缺省值,从而简化调用:
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

#由于命名关键字参数 city 具有默认值,调用时,可不传入 city 参数:
person('Jack', 24, job='Engineer')

#使用命名关键字参数时,要特别注意, * 不是参数,而是特殊分隔符。
#如果缺少 * ,Python 解释器将无法识别位置参数和命名关键字参数:
def person(name, age, city, job):
    # 缺少 *,city 和 job 被视为位置参数
    pass