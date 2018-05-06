# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:14:02 2018
10 斐波那契数列

要求输入一个整数n，请你输出斐波那契数列的第n项。

@author: situ
"""


def Fibonacci1(n):
    """这种傻瓜式递归效率是非常低的。。。O(2^n)"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci1(n-1)+Fibonacci1(n-2)

def Fibonacci2(n):
    """
    根据剑指offer上的提示自己想的解法
    O(n)的解法:从下往上计算，把已得到的中间项保留起来，避免多次重复计算
    """
    if n==0:
        return 0
    else:
        seq = [0]*(n+1)
        seq[1] = 1
        if n>1:
            for i in range(2,n+1):
                seq[i] = seq[i-1]+seq[i-2]
        return seq[-1]

def Fibonacci3(n):
    """剑指offer上的解法:果然是这个最快"""
    array = [0,1]
    if n<=1:
        return array[n]
    else:
        for i in range(n-1):
            fn = array[0]+array[1]
            array[0] = array[1]
            array[1] = fn
        return fn

n=100

import time
#start =time.clock()
#
#print(Fibonacci1(n))
#
#end = time.clock()
#print('Running time: %s Seconds'%(end-start))
    
start =time.clock()

print(Fibonacci2(n))

end = time.clock()
print('Running time: %s Seconds'%(end-start))

start =time.clock()

print(Fibonacci3(n))

end = time.clock()
print('Running time: %s Seconds'%(end-start))
            