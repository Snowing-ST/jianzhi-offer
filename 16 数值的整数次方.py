# -*- coding: utf-8 -*-
"""
Created on Wed May  9 21:18:20 2018
16 数值的整数次方

给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

这题看似简单，实际上是考察代码的全面性 

@author: situ
"""

class Solution:
    def Power1(self, base, exponent):
        result = 1
        if exponent>0:
            for i in range(1,exponent+1):
                result*=base
        if exponent<0 and base!=0: 
            for i in range(1,abs(exponent)+1):
                result*=1/base
        if base==0 and exponent<0:#要考虑到指数为负数时，底数不能为0 的情况
            raise ValueError("base can't be zero when exponent is below zero")
        return result

#更高效的代码
#递归，减少乘法次数
#右移，效果等价于除以2，但效率更高
#“与”位运算，效果等价于取2的余数，即判断奇偶，但效率更高
    def Power2(self,base, exponent):
        
        if base==0 and exponent<0:#要考虑到指数为负数时，底数不能为0 的情况
            raise ValueError("base can't be zero when exponent is below zero")
        absExp = abs(exponent)
        if absExp>1:
            
            if absExp & 1==0:#偶数
                result = self.Power2(base,absExp>>1)**2
            else:
                result = self.Power2(base,(absExp-1)>>1)**2*base
        if absExp==1:
            result = base
        if exponent<0:
            result = 1/result

        return result

a = Solution()
exponent=32
base = 5

import time
start =time.clock()

print(a.Power1(base,exponent))

end = time.clock()
print('Running time: %s Seconds'%(end-start))
    
start =time.clock()

print(a.Power2(base,exponent))

end = time.clock()
print('Running time: %s Seconds'%(end-start))