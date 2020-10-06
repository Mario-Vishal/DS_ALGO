def findQuantity(arr):
    
    #we need to find the quantity of water for every block
    
    #first for a block we need to max element on the left side of current element
    
    #and also the right side, after obtaining two values we need to take the minimum
    
    #that min value is subtracted with the height of the block, then this value is water quantity of that block

    lmax=[0]*len(arr) #lmax is the array of elements whose element is left max of the ith element
    rmax=[0]*len(arr) #rmax is the array of elements whose element is right max of the current ith element

    
    max=0
    for i in range(len(arr)-1):
        if max<arr[i]:
            max=arr[i]
        
        lmax[i+1]=max

    max=0
    for i in range(len(arr)-1,0,-1):
        if max<arr[i]:
            max=arr[i]

        rmax[i-1] = max

    total = 0

    for i in range(len(arr)):
                
            val=min(lmax[i],rmax[i]) - arr[i]
            if val>=0:
                total+= val

    return total
                
t = [7,4,0,9]
t1 = [10,8,0,8,2,4,5,5,1]
# t1 = [6,9,9,0,1]
t1 = [1, 9, 5, 3, 2, 5, 2, 5, 8,6,7]

# print(findQuantity(t))
print(findQuantity(t))