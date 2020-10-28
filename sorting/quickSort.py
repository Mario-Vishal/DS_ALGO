def quickSort(l,low,high):

    if low<high:

        p = partition(l,low,high)

        
        quickSort(l,low,p-1)
        quickSort(l,p+1,high)



def partition(l,low,high):
    pivot = l[high]
    i = low-1

    for j in range(low,high):

        if l[j]<=pivot:
            i+=1
            l[i],l[j] = l[j],l[i]

    l[i+1],l[high] = l[high],l[i+1]

    return i+1


l=[23,4,5,12,3,44,5,6,80]

quickSort(l,0,len(l)-1)

print(l)