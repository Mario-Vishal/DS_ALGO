'''
Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}  

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20} 
'''
#---------HARD----------#


#method approach "gap method -- BEST"
#time complexity - 0(nlogn) n -> is size of both arrays traversing and logn -> is the
# no. of gaps as gaps are divided by 2 on every step. 



#below is best method using gap technique.

import math

def merge(arr,arr1):
    
    gap = math.ceil((len(arr)+len(arr1))/2)-1
    left = 0
    right = gap
    rfull=False
    lfull=False
    flag=True

    while gap>0:
    
        if left<len(arr) and right<len(arr) and not rfull and not lfull:
            if arr[left]>arr[right]:
                arr[left],arr[right]=arr[right],arr[left]

            left+=1
            right+=1
            continue

        if left>len(arr)-1 and not lfull:

            lfull = True

        if right>len(arr)-1 and not rfull:

            rfull = True

        if lfull and rfull:

            if flag:
                left=0
                right=gap
                flag=False

            if right<len(arr1):
                if arr1[left]>arr1[right]:
                    arr1[left],arr1[right]=arr1[right],arr1[left]
                left+=1
                right+=1

            else:
                if gap==1:
                    break
                gap=math.ceil(gap/2)
                left=0
                right=gap
                lfull=False
                rfull=False
                flag=True

        elif rfull:
            if right>len(arr1)-1:
                right=0
            
            if arr[left]>arr1[right]:

                arr[left],arr1[right]=arr1[right],arr[left]

            right+=1
            left+=1

        # print(arr,arr1)

    print(arr,arr1)


arr=[1, 4, 4,5, 9, 10, 15, 20,0]
arr1 = [2, 3, 8,8,8, 13,13]

merge(arr,arr1)



