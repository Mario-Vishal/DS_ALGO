#https://youtu.be/wSq_3WieOiw
'''
The question is in the link above and it is a TCS DIGITAL ADVANCED QUESTION
'''

def getMinWeight(arr,n):

    row=0
    column=0
    weight=1

    while True:

        if row<n-1 and column<n-1:

            if arr[row][column+1] > arr[row+1][column]:
                weight=max(weight,arr[row+1][column])
                row+=1
            else:
                weight=max(weight,arr[row][column+1])
                column+=1

        else:

            if row>=n-1 and column>=n-1:
                break

            if row==n-1 and column+1!=n-1:
                
                weight = max(weight,arr[row][column+1])
                column+=1

            elif column==n-1 and row+1!=n-1:
                
                weight =max(weight,arr[row+1][column])
                row+=1
            else:
                row+=1
                column+=1
    

        
    print(weight)

arr = [[1,8,21,7],[19,17,10,20],[2,18,23,22],[14,25,4,13]]
n=4

getMinWeight(arr,n)









