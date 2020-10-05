#AMAZON

'''
Given an array arr[] of positive integers of size N.
Reverse every sub-array of K group elements
'''

#Time Complexity : O(n*k) n-size of array, k - length of the group
#Space Complexity : O(1)

def reverseGroup(arr,k):
    ptr=k-1
    i=0
    if k<len(arr):
        while ptr<len(arr) and i<len(arr):
            j=ptr
            print(j,ptr)
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            i=ptr+1
            ptr+=k
            if ptr>len(arr)-1:
                ptr=len(arr)-1
    else:
        j=len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        
    print(*arr)

arr = [10,20,30,40,50,60]


reverseGroup(arr,2)
print(arr)