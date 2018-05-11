# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:21:01 2018
18 删除链表中重复的结点

@author: situ
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        