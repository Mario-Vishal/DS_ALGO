def InsertionSort(l):

    for i in range(1,len(l)):
        key = l[i]

        j=i-1
        while j>=0 and key<l[j]:
            l[j+1] = l[j]
            j-=1
        
        l[j+1] = key
        


l=[23,12,11,1]

InsertionSort(l)

print(l)
