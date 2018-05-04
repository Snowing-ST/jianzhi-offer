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
        
#方法一：简单的排序
def duplicate(numbers,duplication):
    #此处写排序算法


#方法三：交换数字
def duplicate(numbers,duplication):
    