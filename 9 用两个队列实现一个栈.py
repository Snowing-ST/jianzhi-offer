# -*- coding: utf-8 -*-
"""
Created on Sun May  6 12:39:38 2018
9 用两个队列实现一个栈

不知道对不对。。。

@author: situ
"""
class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, node):
        # write code here
        self.queue1.append(node)
    def pop(self):
        # return xx
        if self.queue1!=[] and self.queue2==[]:#如果stack2为空，则把stack1里的元素全倒进stack2
            for i in self.queue1[::-1]:
                self.queue2.append(i)
                self.queue1=[]
            return self.queue2.pop(0)
        if self.queue1==[] and self.queue2!=[]:
            return self.queue2.pop(0)
        if self.queue1!=[] and self.queue2!=[]:
            return self.queue1.pop(0)
        
def main():
    a = Solution()
    a.push("a")
    a.push("b")
    a.push("c")
    print(a.queue1)
    print(a.pop())
    print(a.queue2)
    print(a.queue1)
    print(a.pop())
    print(a.queue2)
    a.push("d")
    print(a.queue1)
    print(a.pop())
    print(a.queue1)
    print(a.queue2)
    print(a.pop())
    print(a.queue1)    
    print(a.queue2)

if __name__ == '__main__':
    main()