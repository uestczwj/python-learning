#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:06:36 2018

@author: zwj
"""

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
#函数 person 除了必选参数 name 和 age 外,还接受关键字参数 kw 。在调用该函数时,可以只传入必选参数:
person('Michael', 30)

#也可以传入任意个数的关键字参数:
person('Bob', 35, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')

'''关键字参数有什么用?它可以扩展函数的功能。比如,在 person 函数里,我们保证能接收到 name 和 age
 这两个参数,但是,如果调用者愿意提供更多的参数,我们也能收到。试想你正在做一个用户注册的功能,除了
用户名和年龄是必填项外,其他都是可选项,利用关键字参数来定义这个函数就能满足注册的需求。
'''

#和可变参数类似,也可以先组装出一个 dict,然后,把该 dict 转换为关键字参数传进去:

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

#当然,上面复杂的调用可以用简化的写法:
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

'''**extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的 **kw 参数, 
kw 将获得一个 dict,注意 kw 获得的 dict 是 extra 的一份拷贝,对 kw 的改动不会影响到函数外的 extra 。
'''






