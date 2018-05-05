# -*- coding: utf-8 -*-
"""
Created on Sat May  5 17:21:15 2018
7 重建二叉树

新知识：list.index(value)可知元素在列表中的位置

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回根结点

@author: situ
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 返回构造的TreeNode根节点
def reConstructBinaryTree(pre, tin):
    if len(pre)==0:
        return None
    elif len(pre)==1:
        return TreeNode(pre[0]) #不是pre[0]哦！！！叶子节点也用 TreeNode表示，而不是一个整数表示
    else:
        t = TreeNode(pre[0])
        tin_left = tin[:tin.index(t.val)]
        tin_right = tin[tin.index(t.val)+1:]
        pre_left = pre[1:len(tin_left)+1]
        pre_right = pre[len(tin_left)+1:]
        t.left = reConstructBinaryTree(pre_left, tin_left)
        t.right = reConstructBinaryTree(pre_right, tin_right)
        return t
pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]