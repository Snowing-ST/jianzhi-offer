# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:39:04 2018
14 剪绳子

给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)
每段绳子的长度记为k[0],k[1],...,k[m].请问k[0]*k[1]*...*k[m]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.

@author: situ
"""

#动态规划 —————————————————————————————————————————————————————————

#m<=n，当m=n时，乘积为1
#定义f(n)为长度为n的绳子切成若干段之后的子绳子乘积最大值，其中f(1)=1
#f(n) = max(f(i)*f(n-i)) i>=2 n-i>=2 
#当n=2 m=2时，乘积 f(2) = 1
#当n=3 m=2 乘积 2
#当n=3 m=3 乘积 1 f(3) = 2 
#当n=4 m=2 乘积 4 3
#当n=4 m=3 乘积 3
#当n=4 m=4 乘积1 f(4) = 4
#f(5) = max(f(i)*f(5-i)) f(5)=6
def maxProductAfterCutting1(length):
    if length<2:
        return 0
    if length==3:
        return 1
    if length==3:
        return 2
    seq = [0]*(length+1)
    seq[0] = 0
    seq[1] = 1
    seq[2] = 2
    seq[3] = 3 
    for j in range(4,length+1):
        seq[j] = max(seq[i]*seq[j-i] for i in range(1,j))
    return seq[length]

#贪婪算法--------------------------------------------------------
#当n>=5时，应当尽可能剪成多个长度为3的绳子

#递归
#Python确实有递归次数限制，默认最大次数为1000
def maxProductAfterCutting2(length):
#代码其实有问题，1-3的答案不对，懒得改了
    maxlen = length
    if length>=5:
        maxlen = 1
        maxlen*=3*maxProductAfterCutting2(length-3)    
        
    return maxlen
    
#循环 ：把f(n)分解为3**x和y*f(n-3*x)  x>=1,  y=0 or 1, n-3*x=2 or 4,
def maxProductAfterCutting3(length):
    if length<2:
        return 0
    if length==3:
        return 1
    if length==3:
        return 2
    x,y = getXY(length)
    maxlen = 3**x*y
        
    return maxlen

def getXY(length):
    X = length//3
    Y = length%3
    if Y==1:#余数为1时，余数改4
        X-=1
        Y=4
    if Y==0:#余数为0时，为了相乘不受影响而改为1
        Y=1
    return X,Y

n=1999
import time

start =time.clock()
maxProductAfterCutting1(n)
end = time.clock()
print('Running time: %s Seconds'%(end-start))
    
start =time.clock()
maxProductAfterCutting2(n)
end = time.clock()
print('Running time: %s Seconds'%(end-start))

start =time.clock()
maxProductAfterCutting3(n)
end = time.clock()
print('Running time: %s Seconds'%(end-start))    

#n=1999
#Running time: 0.8948084921433406 Seconds
#Running time: 0.00037660433736164123 Seconds
#Running time: 4.551109782369167e-06 Seconds    