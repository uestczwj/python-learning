#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:52:50 2018

@author: zwj
"""
'''  list sort is in-place sort  '''
li = list(range(0, 11))

for i in li:
    if li[i] % 2 == 0:
        li[i] = -li[i]

print('li=', li)
print('li.sort()=', li.sort())
print('li=', li)

students = []

while True:
    name = input("please enter your name('q' or 'Q' to exit) : ")
    if (name ==  'q') or name == 'Q': break
    
    age  = input('please enter your age : ')

    s = {'name': name, 'age': age}
    
    students.append(s)

for stu in students:
    print("{}'s age is {}".format(stu['name'], stu['age']))