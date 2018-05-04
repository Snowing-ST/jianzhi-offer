#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:41:40 2018
数组中重复的数字

@author: situ
"""

#方法二：哈希表

def duplicate(numbers,duplication):
    d = {}
    for i in numbers:
        if i in d:
            duplication[0] = i
            return True
        d[i]=True
    return False
        
#方法一：简单的排序后进行遍历
def duplicate(numbers,duplication):
    #此处写排序算法
    pass


#方法三：交换数字,未通过
def duplicate(numbers,duplication):
    i=0
    while i<len(numbers):
        if i<numbers[i]:
            t = numbers[numbers[i]]
            numbers[numbers[i]] = numbers[i]
            numbers[i] = t
        elif i==numbers[i]:
            i=i+1
        else:
            print(numbers[i])
            duplication[0] = numbers[i]
            return True
    return False

numbers = [2,3,1,0,2,5,3]
duplication=[0]

    