j #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:41:40 2018
数组中重复的数字1

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 

例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

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
    numbers.sort()
    for i in range(1,len(numbers),1):
        if numbers[i]==numbers[i-1]:
            duplication[0]=numbers[i]
            return True
    return False



#方法三：交换数字,即边排序边找重复。运行时间最短
def duplicate(numbers,duplication):
    i=0
    while i<len(numbers):
        #print(i)
        if (i<numbers[i]) & (numbers[i]!=numbers[numbers[i]]):#坑啊，再加上numbers[i]!=numbers[numbers[i]]才对啊！！！！
            t = numbers[i]
            numbers[i] = numbers[t]
            numbers[t] = t
        elif i==numbers[i]:
            i=i+1
        else:
            print(numbers[i])
            duplication[0] = numbers[i]
            return True
    return False

numbers = [2,3,1,0,2,5,3]
duplication=[0]

    