# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:02:24 2018
二维数组中的查找

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
@author: situ
"""

array = [[1,2,8,9],
         [2,4,9,12],
         [4,7,10,13],
         [6,8,11,15]]

target = 7
target = 5


#基于右上角的查找
def Find(target, array):
    n = len(array)
    p = len(array[0])
    while (n>=1) & (p>=1):
        if target<array[0][p-1]:#小于右上角则剔除列
            array = [row[:p-1] for row in array]
            p = p-1
        elif target>array[0][p-1]:#大于右上角则剔除行
            array = array[1:n]
            n=n-1
        else:
            return True
    return False
        
    

