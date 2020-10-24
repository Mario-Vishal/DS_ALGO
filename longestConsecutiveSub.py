'''
Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements 
in the subsequence are consecutive integers, the consecutive numbers can be in any order.


Example:
Input:
2
7
2 6 1 9 4 5 3
7
1 9 3 10 4 20 2

Output:
6
4

Explanation:
Testcase 1:  The consecutive numbers here are 1, 2, 3, 4, 5, 6.
These 6 numbers form the longest consecutive subsquence.
'''


def longSub(arr):
    
    dict= {}
    max_count=-float('inf')
    count = 1
    
    for i in arr:
        dict[i]=True
        
    for i in range(len(arr)):
        
        if not dict.get(arr[i]-1):
            
            curr=arr[i]
            while dict.get(curr+1):
                
                curr+=1
                count+=1
                
                
        max_count = max(max_count,count)
        count=1
        
    return max_count
    
n=int(input())

for _ in range(n):
    
    k=int(input())
    l=list(map(int,input().split()))
    print(longSub(l))