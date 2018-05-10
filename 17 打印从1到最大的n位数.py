# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:50:00 2018
17 打印从1到最大的n位数

@author: situ
"""

def Print1ToMaxOfNDigits_1(n):
    Max = int("9"*n)
    for i in range(1,Max+1):
        print(i)