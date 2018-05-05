# -*- coding: utf-8 -*-
"""
Created on Sat May  5 13:13:37 2018
数组中重复的数字2

不修改数组找出重复的数字

在一个长度为n+1的数组里的所有数字都在1到n的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字，但不能修改数组

例如，如果输入长度为7的数组{2,3,5,4,3,2,6,7}，那么对应的输出重复的数字是2或者3.

@author: situ
"""
numbers = [2,3,5,4,3,2,6,7]
duplication=[0]

#复制数组到辅助数组,边复制边找 O(n)的空间
def duplicate(numbers,duplication):
    numbers1 = [0]*len(numbers)
    for i in numbers:
        if numbers1[i]==0:
            numbers1[i] = i
        else:
            print(i)
            return True
    return False
        

#二分法 未完成
def duplicate(numbers,duplication):
    pass

def rangecount(l,m,end,start):
    """统计列表l中从end到start有多少个数字小于等于m"""
    c=0
    for i in range(len(l)):
        if l[i]<=m:
            c=c+1
    return c
    