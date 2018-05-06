# -*- coding: utf-8 -*-
"""
Created on Sat May  5 20:36:03 2018
8 二叉树的下一个结点

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

@author: situ
"""



tin = {8,6,10,5,7,9,11}
pNode = 8
#对应输出应该为:9
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None #指向父结点,不是指向子节点！！不是指向下一个！！！

def GetNext(pNode):
    if pNode.right is not None:#右子树不为空，则下一个结点为其右子树的最左子节点
        temp_right = pNode.right
        while temp_right.left is not None:
            temp_right = temp_right.left
        return temp_right
    else:
        temp_next = pNode
        while temp_next.next is not None:
            if temp_next.next.left==temp_next:#右子树为空，该结点为父节点的左结点，则下一个结点为其父节点
                return temp_next.next
            else:#右子树为空，该结点为父节点的右结点，则下一个结点为：从该结点一直向上追溯父节点，直到有一个父结点为这个父结点的父结点的左子树为止
                temp_next = temp_next.next
        return None

    

        
        
