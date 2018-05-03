#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 16:52:50 2018

@author: zwj
"""

students = []


while True:
    name = input("please enter your name('q' or 'Q' to exit) : ")
    if (name ==  'q') or name == 'Q': break
    
    age  = input('please enter your age : ')

    s = {'name': name, 'age': age}
    
    students.append(s)

for stu in students:
    print("{}'s age is {}".format(stu['name'], stu['age']))