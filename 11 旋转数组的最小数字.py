# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:03:03 2018
11 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
@author: situ
"""

rotateArray = [3,4,5,1,2]

def minNumberInRotateArray(rotateArray):
    """
    其实还没考虑index1 indexMid index2指向的元素均相等的情况
    """
    if len(rotateArray)==0:
        return 0
    elif len(rotateArray)==1:
        return rotateArray[0]
    else:
        index1 = 0
        index2 = len(rotateArray)-1
        if rotateArray[index1]<rotateArray[index2]:#如果开头的元素小于末尾的元素，说明这个数组就是顺序数组
            return rotateArray[index1]
        else:
            while index1<index2-1:
                indexMid = (index1+index2)//2
                if rotateArray[indexMid]>=rotateArray[index1]:
                    #中间的元素位于前半个递增数组,最小的数字位于mid到index2之间
                    index1 = indexMid
                if rotateArray[indexMid]<=rotateArray[index2]:
                    #中间的元素位于后半个递增数组,最小的数字位于index1到mid之间
                    index2 = indexMid
        return rotateArray[index2]
        
    