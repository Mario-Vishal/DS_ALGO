'''
Given an array arr[] denoting heights of N towers and a positive integer K, modify the heights of each tower either by increasing or decreasing them by K only once. Find out the minimum difference
of the heights of shortest and longest modified towers.



Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.


'''


def minJumps(arr):
    
    n=len(arr)
    
    res = [0 for i in range(n)]
    

    for i in range(1,n):
        
        res[i]=float('inf')
        
        for j in range(i):
            
            if j+arr[j]>=i:
                
                res[i] = min(res[j]+1,res[i])
                break
            

            
    if res[n-1]!=float('inf'):
        return res[n-1]
        
    else:
        return -1


arr = [1,3,5,8,9,2,6,7,6,8,9]
print(minJumps(arr))