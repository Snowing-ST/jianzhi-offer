# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:14:23 2018
9 用两个栈实现队列

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

@author: situ
"""

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack1!=[] and self.stack2==[]:#如果stack2为空，则把stack1里的元素全倒进stack2
            for i in self.stack1:
                self.stack2.append(i)
                self.stack1=[]
        return self.stack2.pop(0)

def main():
    a = Solution()
    a.push("a")
    a.push("b")
    a.push("c")
    print(a.stack1)
    print(a.pop())
    print(a.stack2)
    print(a.stack1)
    print(a.pop())
    print(a.stack2)
    a.push("d")
    print(a.pop())

if __name__ == '__main__':
    main()
