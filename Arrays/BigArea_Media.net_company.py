'''
Biggest Square 

you are given a matrix A of R rows and C columns. Each cell is colored which is white and black i.e 0 and 1 respectively.

input : A -> matrix, B -> row value C -> Column Value D -> integer

given these values (B,C) are coordinates in the matrix A we need to find the area of the square where the area should contain atmost D ones in it
and also the (B,C) should be the center of the square

constraints:
-the sides must be odd
-numbering row starts from top to bottom
-numbering col starts from left to right

output:
 area of the square which conatins atmost D number of ones in it's area.

 Approach :

    1.need to check all the sides of the center and increase the length of the side gradually

        - we need to check if the left , right ,top , bottom exits for the center (B,C)

    2.after checking all the sides we will use checkOnes function which will take the inputs of extreme top left coordinates of the area we just found
        by checking left,right,top,bottom and also the extreme bottom right coordinates with the matrix itself.

        - it will traverse and find the number of ones.

    3.getting number of ones we will check if the number is less than D.
        - if it is it continues
        - else if it is equal to D it breaks
        - if it is more than D
            -  the sides will be reduced by 1 because of the atmost condition

    4.after exiting while loop we check if the sides are odd if not we reduce it by 1
        -if both are not equal we return the square of min of both sides.

'''

#Time Complexity - O(n*n)
#space complexity - O(1)



class Solution:
    
    def solveUtil(self,A,B,C,D):

        
            top=[B-1,C-1]
            right=[B-1,C-1]
            left=[B-1,C-1]
            bottom=[B-1,C-1]

            condition=True
            sidel=1
            sidew=1
            maxBlack=0

            r = len(A)
            c = len(A[0])

            while condition:

                top=[top[0]-1,top[1]]
                if top[0]>=0 and top[0]<r:
                    sidel+=1
                else:
                    break

                right=[right[0],right[1]+1]
                if right[1]>=0 and right[1]<c:
                    sidew+=1
                else:
                    break

                bottom=[bottom[0]+1,bottom[1]]
                if bottom[0]>=0 and bottom[0]<r:
                    sidel+=1
                else:
                    break

                left = [left[0],left[1]-1]
                if left[1]>=0 and left[1]<c:
                    sidew+=1
                else:
                    break

                n=top[0]
                m=left[1]

                x=bottom[0]
                y=right[1]

                maxBlack=self.checkOnes(A,n,m,x,y)
            
                if maxBlack<D:
                    continue
                elif maxBlack==D:
                    break
                else:
                    sidel-=1
                    sidew-=1
                    break
            
            
            if sidel%2==0:
                sidel-=1
            if sidew%2==0:
                sidew-=1

           
            return sidel*sidew


    def checkOnes(self,A,n,m,x,y):
        black=0

        for i in range(n,x+1):
            for j in range(m,y+1):
                
                if A[i][j]==1:
                    black+=1

        return black


c = Solution()
A=[[0,1,0,1,1,0,1],[0,1,0,1,0,1,0],[0,1,0,1,0,1,1],[0,1,1,1,1,1,0],[0,0,0,0,0,0,0]]
print(c.solveUtil(A,3,4,5))
            






