def findSub(arr):
    
    seen = set()
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum in seen or sum==0:
            return 'Yes'
        else:
            seen.add(sum)
            
    return 'No'
    
n=int(input())
for _ in range(n):
    
    m = int(input())
    l = list(map(int,input().split()))
    
    print(findSub(l))