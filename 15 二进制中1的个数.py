# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:42:28 2018
15 二进制中1的个数

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示

@author: situ
"""

#书上的代码1 可能陷入死循环
def NumberOf1(n):
    count = 0
    while n:
        if n & 1: #判断n的二进制的末尾是不是1
            count+=1 #是的话就加1
            n=n>>1 #n转化为二进制后右移一位，又转化成10进制
    return count