# -*- coding: utf-8 -*-
"""
Created on Sun May  6 16:59:50 2018
12 矩阵中的路径

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

@author: situ
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        visited = [0]*rows*cols
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix,rows,cols,row,col,path,visited,pathLength):
                    return True
        return False
    
    def hasPathCore(self,matrix,rows,cols,row,col,path,visited,pathLength):
        if pathLength==len(path):
            return True
        haspath=0
#        print(row,col,pathLength)
        if row<rows and col<cols and row>=0 and col>=0 \
            and matrix[row*cols+col]==path[pathLength] and visited[row*cols+col]==0:
            pathLength +=1
            visited[row*cols+col] = 1
            haspath = self.hasPathCore(matrix,rows,cols,row+1,col,path,visited,pathLength) \
                    or self.hasPathCore(matrix,rows,cols,row-1,col,path,visited,pathLength)\
                    or self.hasPathCore(matrix,rows,cols,row,col+1,path,visited,pathLength)\
                    or self.hasPathCore(matrix,rows,cols,row,col-1,path,visited,pathLength)
            if haspath==0:
                pathLength -=1
                visited[row*cols+col] = 0
        return haspath
        
def main():
    matrix, rows, cols, path = "ABCESFCSADEE",3,4,"ABCCED"
    a = Solution()
    print(a.hasPath(matrix, rows, cols, path))

if __name__=="__main__":
    main()

