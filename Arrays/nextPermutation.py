def nextPermute(arr):

    index1=-1
    index2=-1
    n=len(arr)-1
    for i in range(n,0,-1):

        if arr[i-1]<arr[i]:
            index1=i-1
            break

    if index1==-1:
        return reverse(arr,0,n)

    for i in range(n,-1,-1):

        if arr[index1]<arr[i]:
            index2=i
            break

    arr[index1],arr[index2]=arr[index2],arr[index1]

    arr = reverse(arr,index1+1,n)
    
    return arr
 

def reverse(arr,i,j):

    while i<j:

        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

    return arr


arr = [1,2,3,4,5]

v = nextPermute(arr)

print(v)