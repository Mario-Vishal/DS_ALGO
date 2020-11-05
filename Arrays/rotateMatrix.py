def rotateMatrix(matrix):

    n=len(matrix[0])

    for i in range(n):
        for j in range(i):

            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    

    for i in range(n):
            temp=0
            temp1=n-1 
            while temp<temp1:
                matrix[i][temp],matrix[i][temp1] = matrix[i][temp1],matrix[i][temp]
                temp1-=1
                temp+=1
    
    return matrix

def printM(matrix):
    n=len(matrix[0])
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end =" ")
        print()


matrix = [[1,2,3],[4,5,6],[7,8,9]]


rotateMatrix(matrix)

printM(matrix)