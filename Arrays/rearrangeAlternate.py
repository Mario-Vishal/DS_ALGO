'''
Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0} 
'''

def rightRotate(arr,outofplace,curr):

    tmp = arr[curr]
    for i in range(curr,outofplace,-1):
        arr[i]=arr[i-1]

    arr[outofplace]=tmp

def rearrangeAlt(arr):

    outofplace = -1
    index=0
    while index<len(arr):

        #the below line means that we found an outof place element
        if outofplace>=0:

            if arr[index]>=0 and arr[outofplace]<0 or arr[index]<0 and arr[outofplace]>=0:

                rightRotate(arr,outofplace,index)

                if index-outofplace >=2 :
                    outofplace+=2
                else:
                    outofplace=-1

        #it  means no element found out of place yet
        if outofplace == -1:

            #check if the current element at that index is outofplace
            if arr[index]>=0 and index%2==0 or arr[index]<0 and index%2!=0:
                outofplace=index

        index+=1
    return arr


arr = [1,2,3,-4,-1,-4]
v = rearrangeAlt(arr)
print(v)
        


