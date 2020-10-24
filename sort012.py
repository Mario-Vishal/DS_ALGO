#sort 0's 1's and 2's

#Time Complexity - O(n)
#Space Complexity - O(1)

#Algorithm - Dutch Flag Method

def sort012(l):
    
    low=0
    mid=0
    high=len(l)-1
    
    while mid<=high:

        
        if l[mid]==0:
            pos1 = mid
            pos = low
            mid+=1 
            
            low+=1

        elif l[mid]==1:
            mid+=1
            continue

        elif l[mid]==2:
            pos=mid
            pos1=high
            high = high-1



        l[pos],l[pos1]=l[pos1],l[pos]
            
        
        

        # if l[high]==1:
        #     l[mid],

        print(l)

        # if l[high]==0:
        #     l[low],l[high]=l[high],
            
    return l
l=[0,2,1,2,0,1,0,0]
sort012(l)
print(l)