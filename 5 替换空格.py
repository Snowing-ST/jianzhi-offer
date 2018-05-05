# -*- coding: utf-8 -*-
"""
Created on Sat May  5 14:41:43 2018
替换空格

请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

@author: situ
"""



s = "We Are Happy"

#醉了，这也行。。。。。。
def replaceSpace(s):
#    return ("%20").join(s.split(' '))
    return s.replace(' ','%20')
