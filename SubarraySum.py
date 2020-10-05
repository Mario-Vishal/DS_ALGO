def findSubarray(arr,k):
    
    sum=0
    pointer=0
    i=0
    while i<len(arr):
        
        if sum+arr[i]<=k:
            sum+=arr[i]
        else:
            sum+=arr[i]
            while pointer<i:

                sum-=arr[pointer]
                pointer+=1
                if sum<=k:
                    break      
        if sum==k:
            print(pointer+1,i+1)
            return
        i+=1
        
    print(-1)

arr = list(map(int,'193 55 70 82 66 68 114 194 35 73 173 31 102 43 178 78 171 103 165 182 191 24 38 24 180 196 170 128 43 111 183 59 127 88 71 129 52 59 14 61 184 87 143 11 73 129 35 42 119 104 68'.split(' ')))
arr = [1,2,3,7,5]
print(findSubarray(arr,1))