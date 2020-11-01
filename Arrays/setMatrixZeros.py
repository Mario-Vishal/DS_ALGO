'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
#medium - leetcode

def setMatrixZero(matrix):

    m,n = len(matrix),len(matrix[0])
    col=False
    for i in range(m):
        if matrix[i][0]==0:
            col=True
        for j in range(1,n):
            if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    

    for i in range(m-1,-1,-1):
        for j in range(n-1,0,-1):

            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

        if col:
            matrix[i][0]=0


def printM(arr):

    for i in range(len(arr)):
        for j in range(len(arr[0])):

            print(arr[i][j],end=" ")
        print()


 
matrix = [[1,2,1,0],[1,0,1,1],[1,1,1,1],[1,1,1,1]]
vb = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

m = [[1,1,0],[1,1,1]]

setMatrixZero(matrix)

printM(matrix)
                


