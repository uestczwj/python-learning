#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:02:42 2018

@author: zwj
"""

index    = 0
students = {}

while True:
    name = input("please enter your name('q' or 'Q' to exit) : ")
    if (name ==  'q') or name == 'Q': break
    
    age  = input('please enter your age : ')

    s = {'name': name, 'age': age}
    
    students[index] = s      
    index +=1

"""
0 : {'name': 'zwj', 'age': '21'}
1 : {'name': 'xxl', 'age': '8'}
2 : {'name': 'hjj', 'age': '23'}
"""

for index in range(len(students)):
    stu = students[index]
    print("{}'s age is {}".format(stu['name'], stu['age']))

for stu in students.values():
    print("{}'s age is {}".format(stu['name'], stu['age']))
    
"""
zwj's age is 21
kxl's age is 8
hjj's age is 23
"""
    
    