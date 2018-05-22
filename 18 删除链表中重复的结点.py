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

#


#自己写的用递归的方式，把列表转换为链表，但不知道哪里有问题，没通过测试，最后少了一位
def buildList1(List):
    if List == []:#考虑特殊情况：列表为空应该返回None值
        return None
    pNode = ListNode(List[0])
    if len(List)>1:
        pNode.next = buildList1(List[1:])
    return pNode


#先不管三七二十一把所有节点的值放到一个列表中，再筛选出值数量为1的值。
#再新建一个链表返回即可。很暴力。
def deleteDuplication(pHead):
    mylist = [] 
    while pHead is not None:
        mylist.append(pHead.val)
        pHead = pHead.next
    unique = [mylist[i] for i in range(len(mylist)) if mylist.count(mylist[i])==1]
    b = buildList1(unique)
    return b

def printListNode(result):
    while result  is not None:
        print(result.val)
        result  = result.next

def buildList2(List): #牛客网讨论区中，别人写的用循环方式把列表变成链表
    dummy = ListNode(0)
    pre = dummy 
    for i in List:
        node = ListNode(i)
        pre.next = node #pre有了next 使得dummy有了next
        #但pre用“=”赋值，dummy不会跟pre一起改变，但它们应该是指向同一个类实体，所以pre的类属性改变，dummy也跟着变
        pre = pre.next 
    return dummy.next

List = [1,2,3,3,4,4,5]
List = [1,1,1,1,1,1,1,1]
pHead = buildList1(List)
pHead = buildList2(List)
result = deleteDuplication(pHead)
printListNode(result)


#牛客网上递归的思路
def deleteDuplication(pHead):
    if pHead.next is not None:
        if pHead.next.val==pHead.val:
            pHead.next=pHead.next.next
            current = pHead
            res = deleteDuplication(current)
        else:
            current = pHead.next
            pHead.next = deleteDuplication(current)
    return res