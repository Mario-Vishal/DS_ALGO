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
        
        #checking if both left pointer and right pointer are pointing to the same first arr.
        if left<len(arr) and right<len(arr) and not rfull and not lfull:
            if arr[left]>arr[right]:
                arr[left],arr[right]=arr[right],arr[left]

            left+=1
            right+=1
            #if this block exectues it skips the below code as it will create unecessary bugs
            continue
        
        #checking if the left pointer crossed the first array if so then setting lfull to true
        if left>len(arr)-1 and not lfull:

            lfull = True
        #checking if the right pointer crossed the first array if so then setting rfull to true
        if right>len(arr)-1 and not rfull:

            rfull = True

        #if both are crossed
        if lfull and rfull:

            #it only checks for the first excecution of the if block
            #to set both left and right according to the second array
            if flag:
                left=0
                right=gap
                flag=False

            #checking if the right pointer is valid
            if right<len(arr1):
                if arr1[left]>arr1[right]:
                    arr1[left],arr1[right]=arr1[right],arr1[left]
                left+=1
                right+=1

            else:
                #if gap is 1 then it breaks
                if gap==1:
                    break
                #else it sets everything to default as we initialised at the beginning
                gap=math.ceil(gap/2)
                left=0
                right=gap
                lfull=False
                rfull=False
                flag=True

        #only if right is crossed
        elif rfull:
            #if right is greater than the length of the second array
            #it sets to right to 0 for second array you can this only
            # executes when right crossed the first array for the first time
            if right>len(arr1)-1:
                right=0
            
            if arr[left]>arr1[right]:

                arr[left],arr1[right]=arr1[right],arr[left]

            right+=1
            left+=1

        # print(arr,arr1)

    print(arr,arr1)


arr1=[1, 4, 4,5, 9, 10, 15, 20,0]
arr = [2, 3, 8,8,8, 13,13]

merge(arr,arr1)



