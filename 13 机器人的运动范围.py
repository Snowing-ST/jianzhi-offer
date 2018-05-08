# -*- coding: utf-8 -*-
"""
Created on Tue May  8 08:39:19 2018
13 机器人的运动范围

地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？

@author: situ
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        visited = [0]*rows*cols
        if threshold==0:
            count = 1
        else:
            count = 0 #初始化
            count = self.movingCountCore(threshold, rows, cols,0,0,count,visited)
        return count

    def movingCountCore(self,threshold, rows, cols,row,col,count,visited):
        count=0 #记累加量
        if row>=0 and row<rows and col>=0 and col<cols \
            and self.getsum(row)<=threshold and self.getsum(col)<=threshold \
            and self.getsum(row)+self.getsum(col)<=threshold and visited[row*cols+col]==0:
            count+=1
#            print(row,col,count)
            visited[row*cols+col] = 1 #对比起上一题，此处不再是or而是+ 因为count是累积的
            count += self.movingCountCore(threshold, rows, cols,row+1,col,count,visited) \
                    + self.movingCountCore(threshold, rows, cols,row-1,col,count,visited) \
                    + self.movingCountCore(threshold, rows, cols,row,col+1,count,visited) \
                    + self.movingCountCore(threshold, rows, cols,row,col-1,count,visited)

        return count
    
    def getsum(self,num):
        return sum(int(i) for i in str(num))
            

def main():
    a = Solution()
    threshold, rows, cols = 5,10,10
    print(a.movingCount(threshold, rows, cols))
    threshold, rows, cols = 10,1,100
    print(a.movingCount(threshold, rows, cols))

if __name__=="__main__":
    main()
