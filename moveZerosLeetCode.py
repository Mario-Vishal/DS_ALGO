def moveZeros(nums):

    lastSeen=0

    for i in range(len(nums)):

        if nums[i]!=0:
            
            nums[lastSeen]=nums[i]
            lastSeen+=1

    

    for i in range(lastSeen,len(nums)):
        nums[i]=0

    

l=[0,1,0,3,12]
moveZeros(l)

