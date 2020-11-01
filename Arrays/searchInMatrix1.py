class Solution:

    def matSearch(self,mat,N,M,X):

        w = []
        
        for row in range(N):
            
            if mat[row][0] <= X and mat[row][M-1] >= X:
                w.append(row)
                break

        for i in w:
            
            if self.binSearch(mat,i,0,M-1,X):
                return 1
                
        return 0


    def binSearch(self,mat,r,low,high,X):

        if low<=high:
            mid = (low+high)
            
            if mat[r][mid]==X:
                return 1
            
            elif mat[r][mid] > X:
                return self.binSearch(mat,r,low,mid-1,X)

            else:
                return self.binSearch(mat,r,mid+1,high,X)

        else:
            return 0


mat = [[18,21,27,38,55,67]]

s = Solution()

print(s.matSearch(mat,1,6,75))