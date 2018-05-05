# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:06:30 2018
从尾到头打印链表

输入一个链表，从尾到头打印链表每个节点的值。
@author: situ
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
#逆序输出:用列表保存结果
def printListFromTailToHead(listNode):      
    mylist = []
    while listNode is not None:
        mylist.append(listNode.val)
        listNode = listNode.next
    mylist.reverse() #或者mylist[::-1]
    return mylist

    
